SELECT COUNT(*) FROM singers
SELECT COUNT(*) AS total_singers FROM stadium
SELECT Name, Country, Age FROM singers ORDER BY Age DESC
SELECT Name, Country, Age FROM Singer ORDER BY Age DESC
SELECT AVG(age) AS average_age, MIN(age) AS min_age, MAX(age) AS max_age FROM singers WHERE country = 'France'
SELECT AVG(Age) AS Average_Age, MIN(Age) AS Minimum_Age, MAX(Age) AS Maximum_Age FROM singers WHERE Nationality = 'French'
SELECT Name, Release_Year FROM Singer ORDER BY Age ASC LIMIT 1
SELECT Name, Release_Year FROM Songs WHERE Singer_ID = (SELECT Singer_ID FROM Singers ORDER BY Age LIMIT 1)
SELECT DISTINCT Country FROM Singers WHERE Age > 20
SELECT DISTINCT Country FROM singers WHERE Age > 20
SELECT Country, COUNT(Singer) AS Number_of_Singers FROM Singers GROUP BY Country;
SELECT COUNT(singer_name) AS num_singers, country FROM singers GROUP BY country;
SELECT Name FROM singers WHERE Age > (SELECT AVG(Age) FROM singers)
SELECT Name FROM stadium WHERE Average > (SELECT AVG(Average) FROM stadium)
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000;
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000
SELECT MAX(Capacity) AS Maximum_Capacity, AVG(Capacity) AS Average_Capacity FROM stadium
SELECT AVG(Capacity) AS Average_Capacity, MAX(Capacity) AS Maximum_Capacity FROM stadium
SELECT Name, Capacity FROM stadium WHERE Average = (SELECT MAX(Average) FROM stadium)
SELECT Name, Capacity FROM stadium WHERE Average = (SELECT MAX(Average) FROM stadium)
SELECT COUNT(*) FROM concerts WHERE year = 2014 OR year = 2015
SELECT COUNT(*) FROM concerts WHERE year = 2014 OR year = 2015
SELECT s.Name AS Stadium_Name, COUNT(c.Concert_ID) AS Number_of_Concerts FROM stadium s LEFT JOIN concert c ON s.Stadium_ID = c.Stadium_ID GROUP BY s.Name;
SELECT s.Name AS Stadium, COUNT(c.Concert_ID) AS Num_Concerts_Played FROM stadium s LEFT JOIN concert c ON s.Stadium_ID = c.Stadium_ID GROUP BY s.Name;
SELECT Name, Capacity FROM stadium WHERE Highest >= 2014 ORDER BY Highest DESC LIMIT 1
SELECT Name, Capacity FROM stadium WHERE Highest > 2013 ORDER BY Highest DESC LIMIT 1
SELECT year, COUNT(*) AS num_concerts FROM concerts GROUP BY year ORDER BY num_concerts DESC LIMIT 1;
SELECT year, COUNT(*) as num_concerts FROM concerts GROUP BY year ORDER BY num_concerts DESC LIMIT 1
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert)
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concerts)
SELECT DISTINCT Location FROM stadium WHERE Highest > 40 AND Lowest < 30;
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert WHERE Year = 2014)
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert WHERE Year = 2014)
SELECT Concert.Name, Concert.Theme, COUNT(Singer.Concert_ID) AS Number_of_Singers FROM Concert JOIN Singer ON Concert.Concert_ID = Singer.Concert_ID GROUP BY Concert.Name, Concert.Theme;
SELECT Concert.Name, Concert.Theme, COUNT(Singer.Name) AS Number_of_Singers FROM Concert JOIN Singer ON Concert.Concert_ID = Singer.Concert_ID GROUP BY Concert.Name, Concert.Theme;
SELECT Singer.Name, COUNT(Concert.Concert_ID) AS Number_of_Concerts FROM Singer JOIN Concert ON Singer.Singer_ID = Concert.Singer_ID GROUP BY Singer.Name;
SELECT Name, COUNT(Concert_ID) AS Number_of_Concerts FROM singers JOIN concerts ON singers.Singer_ID = concerts.Singer_ID GROUP BY Name;
SELECT DISTINCT singer_name FROM concerts WHERE year = 2014
SELECT DISTINCT Singer_Name FROM Concerts WHERE Year = 2014
SELECT singer.Name, singer.Nation FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID WHERE song.Name LIKE '%Hey%'
SELECT Singer.Name, Singer.Country FROM Singer JOIN Song ON Singer.Singer_ID = Song.Singer_ID WHERE Song.Title LIKE '%Hey%'
SELECT Name, Location FROM stadium WHERE Stadium_ID IN (SELECT Stadium_ID FROM concerts WHERE Year = 2014) AND Stadium_ID IN (SELECT Stadium_ID FROM concerts WHERE Year = 2015)
SELECT Name, Location FROM stadium WHERE Stadium_ID IN (SELECT Stadium_ID FROM concerts WHERE Year = 2014) AND Stadium_ID IN (SELECT Stadium_ID FROM concerts WHERE Year = 2015)
SELECT COUNT(*) FROM stadium WHERE Capacity = (SELECT MAX(Capacity) FROM stadium)
SELECT COUNT(*) FROM stadium WHERE Capacity = (SELECT MAX(Capacity) FROM stadium)
SELECT COUNT(*) FROM Pets WHERE weight > 10
SELECT COUNT(*) FROM Pets WHERE weight > 10
SELECT MIN(weight) FROM Dogs WHERE age = (SELECT MIN(age) FROM Dogs)
SELECT MIN(Weight) FROM Dogs WHERE Age = (SELECT MIN(Age) FROM Dogs)
SELECT MAX(weight) AS max_weight, pet_type FROM Pets GROUP BY pet_type;
SELECT pet_type, MAX(weight) AS max_weight FROM pets GROUP BY pet_type;
SELECT COUNT(*) AS num_pets FROM Pet p JOIN Student s ON p.StuID = s.StuID WHERE s.Age > 20
SELECT COUNT(*) AS num_pets FROM Pet p JOIN Student s ON p.StuID = s.StuID WHERE s.Age > 20
SELECT COUNT(*) FROM Student WHERE Sex = 'F' AND StuID IN (SELECT StuID FROM Pet WHERE PetType = 'dog')
SELECT COUNT(*) FROM Student WHERE Sex = 'F' AND StuID IN (SELECT StuID FROM Pet WHERE PetType = 'Dog')
SELECT COUNT(DISTINCT type) AS num_distinct_pets FROM Pets
SELECT COUNT(DISTINCT pet_type) AS num_types FROM Pet
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Pet WHERE PetType IN ('cat', 'dog'))
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Pet WHERE PetType = 'cat' OR PetType = 'dog')
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Pets WHERE PetType = 'cat') AND StuID IN (SELECT StuID FROM Pets WHERE PetType = 'dog')
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Pets WHERE PetType = 'cat') AND StuID IN (SELECT StuID FROM Pets WHERE PetType = 'dog')
SELECT Major, Age FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet WHERE PetType = 'cat')
SELECT Major, Age FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet WHERE PetType = 'Cat')
SELECT StuID FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet WHERE PetType = 'cat')
SELECT StuID FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet WHERE PetType = 'Cat')
SELECT Fname, Age FROM Student WHERE StuID IN (SELECT StuID FROM Pets WHERE PetType = 'dog') AND StuID NOT IN (SELECT StuID FROM Pets WHERE PetType = 'cat')
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM StudentPets WHERE PetType = 'dog') AND StuID NOT IN (SELECT StuID FROM StudentPets WHERE PetType = 'cat')
SELECT type, weight FROM Pet ORDER BY age LIMIT 1;
SELECT pet_type, weight FROM Animals ORDER BY age LIMIT 1
SELECT id, weight FROM pets WHERE age > 1
SELECT id, weight FROM pet WHERE age > 1
SELECT AVG(Age) AS average_age, MAX(Age) AS max_age, pet_type FROM Pets GROUP BY pet_type;
SELECT pet_type, AVG(age) AS average_age, MAX(age) AS max_age FROM pets GROUP BY pet_type;
SELECT pet_type, AVG(weight) AS average_weight FROM pets GROUP BY pet_type;
SELECT AVG(weight) AS average_weight, type_of_pet FROM pets_table GROUP BY type_of_pet;
SELECT Fname, Age FROM Student WHERE StuID IN (SELECT StuID FROM Pet)
SELECT DISTINCT Fname, Age FROM Student WHERE StuID IN (SELECT StuID FROM Pets)
SELECT PetID FROM Pet WHERE OwnerID IN (SELECT StuID FROM Student WHERE LName = 'Smith')
SELECT pet_id FROM PetOwnership WHERE student_id IN (SELECT StuID FROM Student WHERE LName = 'Smith')
SELECT StuID, COUNT(*) AS num_pets FROM Pet GROUP BY StuID
SELECT StuID, COUNT(*) AS num_pets FROM Student GROUP BY StuID HAVING COUNT(*) > 0
SELECT Fname, Sex FROM Student WHERE StuID IN (SELECT StuID FROM Pet GROUP BY StuID HAVING COUNT(*) > 1)
SELECT Fname, Sex FROM Student WHERE StuID IN (SELECT StuID FROM Pet GROUP BY StuID HAVING COUNT(*) > 1)
SELECT LName FROM Student WHERE Age = 3 AND StuID IN (SELECT StuID FROM Cats WHERE Age = 3)
SELECT LName FROM Student WHERE StuID IN (SELECT StuID FROM Student WHERE Age = 3 AND StuID IN (SELECT StuID FROM Student WHERE Fname = 'cat')) ORDER BY StuID DESC LIMIT 1
SELECT AVG(Age) FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet)
SELECT AVG(Age) AS average_age FROM Student WHERE StuID NOT IN (SELECT StuID FROM Pet)
SELECT COUNT(*) FROM continents
SELECT COUNT(DISTINCT Continent) AS NumberOfContinents FROM continents;
SELECT continents.ContId, continents.Continent, COUNT(countries.CountryId) AS num_countries FROM continents LEFT JOIN countries ON continents.ContId = countries.ContId GROUP BY continents.ContId, continents.Continent;
SELECT ContId, Continent, COUNT(*) AS NumOfCountries FROM continents GROUP BY ContId, Continent;
SELECT COUNT(DISTINCT Continent) AS NumberOfCountries FROM continents
SELECT COUNT(*) AS country_count FROM continents
SELECT makers.full_name, makers.id, COUNT(models.id) AS number_of_models FROM makers JOIN models ON makers.id = models.maker_id GROUP BY makers.full_name, makers.id;
SELECT car_makers.id, car_makers.full_name, COUNT(models.id) AS num_models FROM car_makers JOIN models ON car_makers.id = models.car_maker_id GROUP BY car_makers.id, car_makers.full_name;
SELECT model FROM cars WHERE horsepower = (SELECT MIN(horsepower) FROM cars)
SELECT Model FROM Cars WHERE Horsepower = (SELECT MIN(Horsepower) FROM Cars)
SELECT Model FROM Cars WHERE Weight < (SELECT AVG(Weight) FROM Cars)
SELECT * FROM car_models WHERE weight < (SELECT AVG(weight) FROM car_models)
SELECT DISTINCT Maker FROM cars WHERE Year = 1970
SELECT DISTINCT Maker FROM Cars WHERE Year = 1970
SELECT make, production_time FROM cars WHERE production_time = (SELECT MIN(production_time) FROM cars)
SELECT maker, MIN(year) FROM cars GROUP BY maker ORDER BY MIN(year) LIMIT 1;
SELECT DISTINCT CarModel FROM Cars WHERE ProductionYear > 1980
SELECT DISTINCT Model FROM cards WHERE ProductionYear > 1980
SELECT Continent, COUNT(*) AS CarMakersCount FROM continents GROUP BY Continent;
SELECT continents.Continent, COUNT(car_makers.CarId) AS num_car_makers FROM continents LEFT JOIN car_makers ON continents.ContId = car_makers.ContId GROUP BY continents.Continent;
SELECT Continent, COUNT(*) AS CarMakers FROM countries GROUP BY Continent ORDER BY CarMakers DESC LIMIT 1
SELECT Continent, COUNT(CarMaker) AS NumCarMakers FROM continents GROUP BY Continent ORDER BY NumCarMakers DESC LIMIT 1
SELECT COUNT(car_model) AS model_count, maker_full_name FROM car_models GROUP BY maker_full_name;
SELECT COUNT(car_models.model) AS number_of_models, makers.maker_id, makers.full_name FROM car_models JOIN makers ON car_models.maker_id = makers.maker_id GROUP BY makers.maker_id, makers.full_name;
SELECT accelerate FROM car_table WHERE make = 'amc hornet sportabout (sw)'
SELECT acceleration FROM cars WHERE car_name = 'amc hornet sportabout (sw)'
SELECT COUNT(DISTINCT Maker) FROM car_makers WHERE Country = 'France';
SELECT COUNT(DISTINCT Maker) FROM care WHERE Country = 'France'
SELECT COUNT(DISTINCT Model) FROM car_table WHERE Country = 'USA';
SELECT COUNT(Model) FROM car_table WHERE Country = 'United States'
SELECT AVG(mpg) FROM cars WHERE cylinders = 4;
SELECT AVG(mpg) FROM cars WHERE cylinders = 4;
SELECT MIN(Weight) FROM cars WHERE Cylinders = 8 AND Year = 1974
SELECT MIN(Weight) FROM cars WHERE Cylinders = 8 AND Year = 1974
SELECT Maker, Model FROM cars
SELECT Maker, Model FROM cars
SELECT c.Name, c.Id FROM countries c WHERE c.Id IN (SELECT DISTINCT cm.CountryId FROM car_makers cm)
SELECT CountryName, CountryId FROM countries WHERE CarMakerCount > 0;
SELECT COUNT(*) FROM cars WHERE horsepower > 150
SELECT COUNT(*) FROM cars WHERE horsepower > 150
SELECT AVG(weight) FROM cars GROUP BY year;
SELECT AVG(weight), year FROM table_name GROUP BY year;
SELECT Continent FROM continents WHERE Continent = 'Europe' GROUP BY Continent HAVING COUNT(*) >= 3;
SELECT CountryName FROM countries WHERE Continent = 'Europe' GROUP BY CountryName HAVING COUNT(DISTINCT Manufacturer) >= 3;
SELECT MAX(Horsepower), Make FROM car_models WHERE Cylinders = 3 GROUP BY Make
SELECT MAX(Horsepower) AS MaxHorsepower, Make FROM models WHERE Cylinders = 3 GROUP BY Make ORDER BY MaxHorsepower DESC LIMIT 1;
SELECT Model FROM Cars ORDER BY MilesPerGallon DESC LIMIT 1
SELECT car_model FROM cars ORDER BY mpg DESC LIMIT 1
SELECT AVG(Horsepower) FROM cars WHERE Year < 1980
SELECT AVG(horsepower) FROM cars WHERE year < 1980
SELECT AVG(edispl) FROM cars WHERE model = 'volvo'
SELECT AVG(edispl) FROM table_name WHERE make = 'Volvo';
SELECT cylinders, MAX(accelerate) AS max_accelerate FROM table_name GROUP BY cylinders;
SELECT MAX(accelerate) FROM table_name GROUP BY cylinders;
SELECT model, COUNT(make) AS num_cars FROM cars GROUP BY model ORDER BY num_cars DESC LIMIT 1;
SELECT model, COUNT(DISTINCT version) AS num_versions FROM table_name GROUP BY model ORDER BY num_versions DESC LIMIT 1;
SELECT COUNT(*) FROM cars WHERE cylinders > 4
SELECT COUNT(*) FROM cars WHERE cylinders > 4
SELECT SUM(Quantity) FROM cars WHERE Year = 1980
SELECT COUNT(*) FROM cars WHERE year = 1980
SELECT COUNT(DISTINCT Model) FROM car_models WHERE MakerFullName = 'American Motor Company'
SELECT COUNT(*) AS num_car_models FROM car_models WHERE car_maker = 'American Motor Company'
SELECT MakerFullName, MakerId FROM car_models GROUP BY MakerFullName, MakerId HAVING COUNT(ModelId) > 3;
SELECT Name, Id FROM makers WHERE Models > 3
SELECT DISTINCT Model FROM Cars WHERE MakerFullName = 'General Motors' OR Weight > 3500
SELECT DISTINCT Model FROM cars WHERE Maker = 'General Motors' OR Weight > 3500
SELECT DISTINCT Year FROM cars WHERE Weight >= 3000 AND Weight <= 4000
SELECT DISTINCT Year FROM Cars WHERE Weight < 4000 AND Weight > 3000
SELECT MAX(Horsepower) FROM cars ORDER BY Accelerate DESC LIMIT 1;
SELECT Horsepower FROM cars ORDER BY Accelerate DESC LIMIT 1
SELECT MIN(Cylinders) FROM volvo WHERE Accelerate = (SELECT MIN(Accelerate) FROM volvo)
SELECT MIN(Cylinders) FROM VolvoModels WHERE Accelerate = (SELECT MIN(Accelerate) FROM VolvoModels)
SELECT COUNT(*) FROM cars WHERE accelerate > (SELECT MAX(horsepower) FROM cars)
SELECT COUNT(*) FROM cars WHERE accelerate > (SELECT MAX(horsepower) FROM cars)
SELECT COUNT(DISTINCT Country) FROM car_makers GROUP BY Country HAVING COUNT(DISTINCT Maker) > 2
SELECT COUNT(*) FROM (SELECT Continent, COUNT(DISTINCT CarMaker) AS NumCarMakers FROM continents GROUP BY Continent HAVING NumCarMakers > 2) AS countries_with_more_than_2_car_makers
SELECT COUNT(*) FROM cars WHERE cylinders > 6
SELECT COUNT(*) FROM cars WHERE cylinders > 6
SELECT model FROM cars WHERE cylinders = 4 ORDER BY horsepower DESC LIMIT 1;
SELECT model FROM cars WHERE cylinders = 4 ORDER BY horsepower DESC LIMIT 1
SELECT car.makeid, car.makename FROM car WHERE car.horsepower > (SELECT MIN(horsepower) FROM car) AND car.cylinders <= 3
SELECT MakeId, MakeName FROM Cars WHERE Horsepower > (SELECT MIN(Horsepower) FROM Cars) AND Cylinders < 4
SELECT MAX(mpg) FROM cars WHERE cylinders = 8 AND year < 1980
SELECT MAX(mpg) FROM cars WHERE cylinders = 8 OR year < 1980
SELECT model FROM cars WHERE weight < 3500 AND manufacturer != 'Ford Motor Company'
SELECT Model FROM cars WHERE Weight < 3500 AND Manufacturer != 'Ford Motor Company'
SELECT Continent FROM continents WHERE Continent NOT IN (SELECT Continent FROM car_makers)
SELECT Continent FROM continents WHERE Continent NOT IN (SELECT Continent FROM car_makers)
SELECT id, maker FROM car_makers GROUP BY id, maker HAVING COUNT(model) >= 2 AND COUNT(DISTINCT maker) > 3;
SELECT CarId, Maker FROM CarMakers WHERE NumModels >= 2 AND NumCars > 3
SELECT id, name FROM countries WHERE id IN (SELECT country_id FROM car_makers GROUP BY country_id HAVING COUNT(DISTINCT car_maker) > 3) OR id IN (SELECT country_id FROM car_models WHERE model = 'fiat')
SELECT id, name FROM countries WHERE car_makers > 3 OR model = 'fiat'
SELECT Country FROM airlines WHERE Airline = 'JetBlue Airways';
SELECT Country FROM airlines WHERE Airline = 'Jetblue Airways'
SELECT Abbreviation FROM airlines WHERE Airline = 'JetBlue Airways';
SELECT Abbreviation FROM airlines WHERE Airline = 'Jetblue Airways';
SELECT Airline, Abbreviation FROM airlines WHERE Country = 'USA';
SELECT Airline, Abbreviation FROM airlines WHERE Country = 'USA';
SELECT AirportCode, AirportName FROM airports WHERE City = 'Anthony';
SELECT AirportCode, AirportName FROM airports WHERE City = 'Anthony';
SELECT COUNT(*) AS total_airlines FROM airlines
SELECT COUNT(*) AS total_airlines FROM airlines
SELECT COUNT(*) FROM airports
SELECT COUNT(*) FROM airports
SELECT COUNT(*) FROM airlines
SELECT COUNT(*) FROM airlines
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL'
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL';
SELECT COUNT(*) FROM airlines WHERE Country = 'USA'
SELECT COUNT(*) FROM airlines WHERE Country = 'USA';
SELECT City, Country FROM airports WHERE Airport = 'Alton'
SELECT City, Country FROM airports WHERE Airport = 'Alton'
SELECT AirportName FROM airports WHERE AirportCode = 'AKO'
SELECT Airline FROM airlines WHERE Abbreviation = 'AKO';
SELECT AirportName FROM airports WHERE City = 'Aberdeen'
SELECT Airline FROM airlines WHERE Country = 'Aberdeen'
SELECT COUNT(*) FROM airlines WHERE Departure = 'APG'
SELECT COUNT(*) FROM airlines WHERE Departure = 'APG';
SELECT COUNT(*) FROM flights WHERE destination = 'ATO';
SELECT COUNT(*) FROM airlines WHERE Country = 'ATO'
SELECT COUNT(*) FROM flights WHERE DepartureCity = 'Aberdeen'
SELECT COUNT(*) FROM airlines WHERE Departure = 'Aberdeen'
SELECT COUNT(*) FROM airlines WHERE City = 'Aberdeen' AND Direction = 'Arriving'
SELECT COUNT(*) FROM airlines WHERE Country = 'Aberdeen' AND Arriving = 1;
SELECT COUNT(*) FROM flights WHERE DepartureCity = 'Aberdeen' AND DestinationCity = 'Ashley'
SELECT COUNT(*) FROM flights WHERE origin = 'Aberdeen' AND destination = 'Ashley'
SELECT COUNT(*) FROM airlines WHERE Airline = 'JetBlue Airways';
SELECT COUNT(*) FROM airlines WHERE Airline = 'Jetblue Airways'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND Airport = 'ASY'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND Country = 'ASY' AND Airport = 'Arriving'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND DepartureAirport = 'AHD'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND Country = 'AHD' AND Abbreviation = 'AHD'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND Country = 'Aberdeen'
SELECT COUNT(*) FROM airlines WHERE Airline = 'United Airlines' AND Country = 'Aberdeen' AND Abbreviation = 'UA'
SELECT City, COUNT(*) AS NumArrivingFlights FROM airlines GROUP BY City ORDER BY NumArrivingFlights DESC LIMIT 1;
SELECT city, COUNT(destination_airport) AS frequency FROM flights GROUP BY city ORDER BY frequency DESC LIMIT 1
SELECT city, COUNT(*) AS num_departing_flights FROM flights GROUP BY city ORDER BY num_departing_flights DESC LIMIT 1;
SELECT source_airport_city, COUNT(source_airport_city) AS frequency FROM airlines GROUP BY source_airport_city ORDER BY frequency DESC LIMIT 1;
SELECT code FROM airports ORDER BY flights DESC LIMIT 1
SELECT Abbreviation AS airport_code FROM airlines GROUP BY Abbreviation ORDER BY COUNT(*) DESC LIMIT 1
SELECT code FROM airports ORDER BY num_flights ASC LIMIT 1;
SELECT code FROM airports ORDER BY flights ASC LIMIT 1;
SELECT Airline, COUNT(*) AS num_flights FROM airlines GROUP BY Airline ORDER BY num_flights DESC LIMIT 1;
SELECT Airline, COUNT(*) AS num_flights FROM airlines GROUP BY Airline ORDER BY num_flights DESC LIMIT 1;
SELECT Abbreviation, Country FROM airlines GROUP BY Abbreviation, Country ORDER BY COUNT(*) ASC LIMIT 1;
SELECT Abbreviation, Country FROM airlines GROUP BY Abbreviation, Country ORDER BY COUNT(*) ASC LIMIT 1;
SELECT Airline FROM airlines WHERE uid IN (SELECT DISTINCT airline_uid FROM flights WHERE departure_airport = 'AHD')
SELECT Airline FROM airlines WHERE SourceAirport = 'AHD'
SELECT Airline FROM airlines WHERE uid IN (SELECT uid FROM flights WHERE arrival_airport = 'AHD')
SELECT Airline FROM airlines WHERE DestinationAirport = 'AHD'
SELECT Airline FROM airlines WHERE Airline IN (SELECT Airline FROM flights WHERE Airport = 'APG') AND Airline IN (SELECT Airline FROM flights WHERE Airport = 'CVO')
SELECT Airline FROM airlines WHERE DepartingAirport = 'APG' INTERSECT SELECT Airline FROM airlines WHERE DepartingAirport = 'CVO';
SELECT Airline FROM airlines WHERE Airline IN (SELECT Airline FROM flights WHERE DepartureAirport = 'CVO') AND Airline NOT IN (SELECT Airline FROM flights WHERE DepartureAirport = 'APG')
SELECT Airline FROM airlines WHERE Departure = 'CVO' AND Airline NOT IN (SELECT Airline FROM airlines WHERE Departure = 'APG')
SELECT Airline FROM airlines GROUP BY Airline HAVING COUNT(*) >= 10;
SELECT Airline FROM airlines GROUP BY Airline HAVING COUNT(*) >= 10;
SELECT Airline FROM airlines GROUP BY Airline HAVING COUNT(*) < 200;
SELECT Airline FROM airlines GROUP BY Airline HAVING COUNT(*) < 200;
SELECT flight_number FROM flights WHERE Airline = 'United Airlines'
SELECT FlightNumber FROM flights WHERE Airline = 'United Airlines'
SELECT flight_number FROM flights WHERE departure_airport = 'APG'
SELECT flight_number FROM flights WHERE departure_airport = 'APG'
SELECT flight_number FROM flights WHERE arrival_airport = 'APG'
SELECT flight_number FROM flights WHERE destination = 'APG'
SELECT flight_number FROM flights WHERE departure_city = 'Aberdeen'
SELECT flight_number FROM flights WHERE departure_city = 'Aberdeen'
SELECT flight_number FROM flights WHERE arrival_city = 'Aberdeen'
SELECT flight_number FROM flights WHERE destination = 'Aberdeen'
SELECT COUNT(*) FROM flights WHERE destination_city = 'Aberdeen' OR destination_city = 'Abilene';
SELECT COUNT(*) FROM flights WHERE destination = 'Aberdeen' OR destination = 'Abilene'
SELECT Airline FROM airlines WHERE Airline NOT IN (SELECT DISTINCT Airline FROM flights)
SELECT Airline FROM airlines WHERE Airline NOT IN (SELECT DISTINCT Airline FROM departing_flights UNION SELECT DISTINCT Airline FROM arriving_flights)
SELECT COUNT(*) AS total_employees FROM employee
SELECT COUNT(*) AS num_employees FROM employee
SELECT Name FROM employee ORDER BY Age ASC;
SELECT Name FROM employee ORDER BY Age ASC
SELECT City, COUNT(*) AS Number_of_Employees FROM employee GROUP BY City;
SELECT City, COUNT(Employee_ID) AS num_employees FROM employee GROUP BY City;
SELECT City FROM employee GROUP BY City HAVING COUNT(*) > 1 AND MAX(Age) < 30
SELECT City FROM employee GROUP BY City HAVING COUNT(*) > 1 AND MAX(Age) < 30;
SELECT City, COUNT(*) AS Number_of_Shops FROM employee GROUP BY City;
SELECT City, COUNT(*) AS Number_of_Shops FROM employee GROUP BY City;
SELECT manager_name, district FROM shop ORDER BY number_of_products DESC LIMIT 1
SELECT manager_name, district FROM shop WHERE shop_id IN (SELECT shop_id FROM sells GROUP BY shop_id ORDER BY COUNT(product_id) DESC LIMIT 1)
SELECT MIN(products) AS min_products, MAX(products) AS max_products FROM (SELECT COUNT(*) AS products FROM stores GROUP BY store_id) AS product_count
SELECT MIN(products) AS min_products, MAX(products) AS max_products FROM (SELECT COUNT(*) AS products FROM shops GROUP BY shop_id) AS product_count
SELECT name, location, district FROM shops ORDER BY number_of_products DESC
SELECT name, location, district FROM shops ORDER BY number_products DESC
SELECT Name FROM stores WHERE number_of_products > (SELECT AVG(number_of_products) FROM stores)
SELECT Name FROM Shops GROUP BY Name HAVING COUNT(Products) > (SELECT AVG(Products) FROM Shops)
SELECT Name FROM employee GROUP BY Name ORDER BY COUNT(*) DESC LIMIT 1
SELECT Name FROM employee WHERE Employee_ID IN (SELECT Employee_ID FROM evaluations GROUP BY Employee_ID ORDER BY COUNT(*) DESC LIMIT 1)
SELECT Name FROM employee ORDER BY one_time_bonus DESC LIMIT 1
SELECT Name FROM employee ORDER BY Bonus DESC LIMIT 1
SELECT Name FROM employee WHERE Employee_ID NOT IN (SELECT Employee_ID FROM awards)
SELECT Name FROM employee WHERE Employee_ID NOT IN (SELECT Employee_ID FROM evaluation)
SELECT Name FROM shop WHERE Shop_ID = (SELECT Shop_ID FROM employee GROUP BY Shop_ID ORDER BY COUNT(*) DESC LIMIT 1)
SELECT Name AS shop_name FROM employee GROUP BY Name ORDER BY COUNT(*) DESC LIMIT 1
SELECT Name FROM shop WHERE shop_id NOT IN (SELECT DISTINCT shop_id FROM employee)
SELECT shop_name FROM shops WHERE NOT EXISTS (SELECT * FROM employees WHERE employees.shop_id = shops.shop_id)
SELECT shop_name, COUNT(Employee_ID) AS num_employees_hired FROM employee GROUP BY shop_name;
SELECT COUNT(Employee_ID) AS num_employees, Name AS shop_name FROM employee GROUP BY Name
SELECT SUM(bonus) AS total_bonus FROM evaluations
SELECT SUM(bonus) AS total_bonus FROM evaluations
SELECT * FROM employee WHERE City = 'hiring'
SELECT * FROM employee WHERE City = 'hiring'
SELECT district FROM stores WHERE products < 3000 AND district IN (SELECT district FROM stores WHERE products > 10000)
SELECT District FROM Shops WHERE Products < 3000 AND District IN (SELECT District FROM Shops WHERE Products > 10000)
SELECT COUNT(DISTINCT City) AS num_locations FROM employee
SELECT COUNT(DISTINCT City) AS num_distinct_store_locations FROM employee
SELECT COUNT(*) AS document_count FROM Ref_Template_Types
SELECT COUNT(*) FROM Ref_Template_Types;
SELECT Template_Type_Code, Template_Type_Description FROM Ref_Template_Types;
