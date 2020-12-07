-- Project Group 4: Aaron Huber and Lisa Bettcher
-- Date:            11/16/2020
-- Project:         Zootopia Management System
-- File Contents:   Database DMQ

--------------------------------------------------------------------------------
-- The following section contains the Database Manipulation Queries for the
-- Zootopia Management System project website. All queries are included that
-- will be used for our site. NOTE: our site uses Python and Flask. SQL syntax
-- uses '%s' as the string variable which follows the ANSI C printf format code.
-- The '%s' code below can be replaced with a string when testing with MariaDB.
--------------------------------------------------------------------------------

-- -- -- -- -- -- -- -- Populate Tables -- -- -- -- -- -- -- -- -- -- -- -- -- -

-- Populate Animals Table:
SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals
       LEFT JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id
       ORDER BY animal_id ASC;

-- Populate Medications Table:
SELECT med_id, name FROM Medications;

-- Populate Animals_Medications Table:
SELECT id, Animals_Medications.animal_id, Animals_Medications.med_id
       FROM Animals_Medications
       INNER JOIN Animals ON Animals_Medications.animal_id = Animals.animal_id
       INNER JOIN Medications ON Animals_Medications.med_id = Medications.med_id;

-- Populate Zookeepers Table:
SELECT zookeeper_id, first_name, last_name FROM Zookeepers;

-- Populate Workdays Table:
SELECT workday_id, day FROM Workdays;

-- Populate Zookeepers_Workdays Table:
SELECT Zookeepers_Workdays.zookeeper_id, first_name, last_name,
       Zookeepers_Workdays.workday_id, day, id
       FROM Zookeepers_Workdays
       INNER JOIN Zookeepers ON Zookeepers_Workdays.zookeeper_id = Zookeepers.zookeeper_id
       INNER JOIN Workdays ON Zookeepers_Workdays.workday_id = Workdays.workday_id
       ORDER BY Zookeepers_Workdays.workday_id, Zookeepers.last_name ASC;

-- -- -- -- -- -- -- -- Add Table Rows -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Add an Animals Row:
-- NOTE VALUE order: animal_id (DEFAULT), type, sex (M/F), name, age, weight, temperament, zookeeper_id
INSERT INTO Animals VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s);

-- Add a Medications Row:
-- NOTE VALUE order: med_id (DEFAULT), name
INSERT INTO Medications VALUES (DEFAULT, %s);

-- Add an Animals_Medications Relationship Row:
-- NOTE VALUE order: id (DEFAULT), animal_id, med_id
INSERT INTO Animals_Medications VALUES (DEFAULT, %s, %s);

-- Add a Zookeepers Row:
-- NOTE VALUE order: zookeeper_id (DEFAULT), first_name, last_name
INSERT INTO Zookeepers VALUES (DEFAULT, %s, %s);

-- Add a Zookeepers_Workdays Relationship Row:
-- NOTE VALUE order: id (DEFAULT), zookeeper_id, workday_id
INSERT INTO Zookeepers_Workdays VALUES (DEFAULT, %s, %s);

-- -- -- -- -- -- -- -- Update Table Rows -- -- -- -- -- -- -- -- -- -- -- -- --

-- Update an Animal Row:
UPDATE Animals SET animal_id = %s, type = %s, sex = %s, name = %s, age = %s, weight = %s, temperament = %s, zookeeper_id = %s WHERE animal_id = %s;

-- Update a Medications Row:
UPDATE Medications SET name = %s WHERE med_id = %s;

-- Update an Animals_Medications Relationship Row:
UPDATE Animals_Medications SET animal_id = %s, med_id = %s WHERE id = %s;

-- Update a Zookeepers Row:
UPDATE Zookeepers SET first_name = %s, last_name = %s WHERE zookeeper_id= %s;

-- Update a Zookeepers/Workdays Relationship Row:
UPDATE Zookeepers_Workdays SET workday_id = %s WHERE zookeeper_id = %s AND workday_id = %s;

-- -- -- -- -- -- -- Delete Table Rows -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Delete an Animals Row:
DELETE FROM Animals WHERE animal_id = %s;

-- Delete a Medications Row:
DELETE FROM Medications WHERE med_id = %s;

-- Delete an Animals_Medications Relationship Row:
DELETE FROM Animals_Medications WHERE animal_id = %s AND med_id = %s;

-- Delete a Zookeepers Row:
DELETE FROM Zookeepers WHERE zookeeper_id = %s;

-- Delete a Zookeepers_Workdays Relationship Row:
DELETE FROM Zookeepers_Workdays WHERE zookeeper_id = %s AND workday_id = %s;

-- -- -- -- -- -- -- Search Animals Table -- -- -- -- -- -- -- -- -- -- -- -- --
-- The following Animals query will return any full rows that contain search
-- string. NOTE: to perform this search in MariaDB replace '%s' below with a
-- string:
SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals
       LEFT JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id
       WHERE animal_id LIKE %s OR type LIKE %s OR sex LIKE %s OR name LIKE %s
       OR age LIKE %s OR weight LIKE %s OR temperament LIKE %s OR IFNULL(last_name, 'NULL') LIKE %s;