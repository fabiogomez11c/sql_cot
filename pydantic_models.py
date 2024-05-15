from pydantic import BaseModel, Field
from typing_extensions import Literal
from typing import Dict, Any, List


class SQLQuery(BaseModel):
    """Generated SQL query"""
    query: str = Field(..., description='Generated SQL query')


class DataRow(BaseModel):
    """Data inside a table"""
    data: Dict[str, Any] = Field(..., description='One row of data, first element is the id')

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a data row from a dictionary"""
        return cls(data=data['data'])

    def create_row(self) -> Dict[str, Any]:
        """Create a row"""
        return self.data


class Table(BaseModel):
    """Table with a list of data"""
    tableName: str = Field(..., description='Name of the table')
    tableData: List[DataRow] = Field(..., description='All the rows of the table')

    def create_table(self) -> List:
        """Create a table"""
        return [row.create_row() for row in self.tableData]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a table from a dictionary"""
        return cls(tableName=data['tableName'], tableData=[DataRow.from_dict(row) for row in data['tableData']])


class Tables(BaseModel):
    """All the tables in the database"""
    tables: Dict[str, Table] = Field(..., description='All the tables in the database')

    def create_tables(self) -> Dict[str, List]:
        """Create all the tables"""
        return {table_name: table.create_table() for table_name, table in self.tables.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create tables from a dictionary"""
        return cls(tables={table_name: Table.from_dict(table) for table_name, table in data.items()})


class LLMEval(BaseModel):
    """Choice"""
    choice: Literal['A', 'B', 'C'] = Field(..., description='Choice between A, B or C')
