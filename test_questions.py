import unittest
from unittest.mock import mock_open, patch
from questions import Question, SetQuestions, read_json_file_with_questions


class TestQuestions(unittest.TestCase):

    def setUp(self):
        # sample json data for testing
        self.sample_json = """
            {
                "questions": [
                    "What is your name?",
                    "How old are you?",
                    "Where do you live?"
                ]
            }
            """

    def test_question_model(self):
        # Test the Question model
        question = Question(question="What is your name?")
        self.assertEqual(question.question, "What is your name?")

    def test_set_questions_model(self):
        # Test the SetQuestions model
        questions = [
            Question(question="What is your name?"),
            Question(question="How old are you?"),
        ]
        set_questions = SetQuestions(set_questions=questions)
        self.assertEqual(len(set_questions.set_questions), 2)
        self.assertEqual(set_questions.set_questions[0].question, "What is your name?")
        self.assertEqual(set_questions.set_questions[1].question, "How old are you?")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"questions": ["What is your name?", "How old are you?"]}',
    )  # see file: 2024-08-18.21-23-17.263.md
    def test_read_json_file_with_questions(self, mock_file):
        # Test reading questions from a JSON file
        result = read_json_file_with_questions("dummy_path.json")

        # Check if the file was opened
        mock_file.assert_called_once_with("dummy_path.json", "r")

        # Check if the correct number of questions were read
        self.assertEqual(len(result.set_questions), 2)

        # Check if the questions were correctly parsed
        self.assertEqual(result.set_questions[0].question, "What is your name?")
        self.assertEqual(result.set_questions[1].question, "How old are you?")

    def test_read_json_file_with_questions_integration(self):
        # Integration test with actual file I/O
        with patch("builtins.open", mock_open(read_data=self.sample_json)):
            result = read_json_file_with_questions("dummy_path.json")

        # Check if the result is an instance of SetQuestions
        self.assertIsInstance(result, SetQuestions)

        # Check if the correct number of questions were read
        self.assertEqual(len(result.set_questions), 3)

        # Check if the questions were correctly parsed
        self.assertEqual(result.set_questions[0].question, "What is your name?")
        self.assertEqual(result.set_questions[1].question, "How old are you?")
        self.assertEqual(result.set_questions[2].question, "Where do you live?")


if __name__ == "__main__":
    unittest.main()
