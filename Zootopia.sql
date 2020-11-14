-- Project Group 4: Aaron Huber and Lisa Bettcher
-- Date:            11/16/2020
-- Project:         Zootopia Management System
-- File Contents:   Database DDQ and Queries

--------------------------------------------------------------------------------
-- The following section contains the Database DDQ for the Zootopia project
-- website. This info was gathered by performing a database dump from MariaDB
-- for the following tables in our project: Animals, Medications, 
-- Animals_Medications, Zookeepers, Workdays, and Zookeepers_Workdays.
--------------------------------------------------------------------------------

-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Linux (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_huberaa
-- ------------------------------------------------------
-- Server version	10.4.15-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Animals`
--

DROP TABLE IF EXISTS `Animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Animals` (
  `animal_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `weight` decimal(18,2) DEFAULT NULL,
  `temperament` varchar(255) DEFAULT NULL,
  `zookeeper_id` int(11) NOT NULL,
  PRIMARY KEY (`animal_id`),
  UNIQUE KEY `animal_id` (`animal_id`),
  KEY `Animals_FK1` (`zookeeper_id`),
  CONSTRAINT `Animals_FK1` FOREIGN KEY (`zookeeper_id`) REFERENCES `Zookeepers` (`zookeeper_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Animals`
--

LOCK TABLES `Animals` WRITE;
/*!40000 ALTER TABLE `Animals` DISABLE KEYS */;
INSERT INTO `Animals` VALUES (1,'Lion','F','Lucy',4,510.30,'Bitey',2),(2,'Monkey','F','Sheryl',10,32.21,'Lovely',1),(4,'Elephant','M','Hank',34,1289.34,'Friendly',3),(5,'Zebra','M','Steve',12,435.87,'Moody',4),(6,'Lion','M','Larry',18,575.98,'Lazy',2);
/*!40000 ALTER TABLE `Animals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medications`
--

DROP TABLE IF EXISTS `Medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medications` (
  `med_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`med_id`),
  UNIQUE KEY `med_id` (`med_id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medications`
--

LOCK TABLES `Medications` WRITE;
/*!40000 ALTER TABLE `Medications` DISABLE KEYS */;
INSERT INTO `Medications` VALUES (1,'Penicillin'),(2,'Xanax'),(3,'Insulin'),(4,'Antiparasitic'),(5,'Steroid'),(6,'Opiod');
/*!40000 ALTER TABLE `Medications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Animals_Medications`
--

DROP TABLE IF EXISTS `Animals_Medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Animals_Medications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `animal_id` int(11) DEFAULT NULL,
  `med_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `Animals_Medications_FK1` (`animal_id`),
  KEY `Animals_Medications_FK2` (`med_id`),
  CONSTRAINT `Animals_Medications_FK1` FOREIGN KEY (`animal_id`) REFERENCES `Animals` (`animal_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Animals_Medications_FK2` FOREIGN KEY (`med_id`) REFERENCES `Medications` (`med_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Animals_Medications`
--

LOCK TABLES `Animals_Medications` WRITE;
/*!40000 ALTER TABLE `Animals_Medications` DISABLE KEYS */;
INSERT INTO `Animals_Medications` VALUES (1,1,3),(3,2,1),(4,2,2);
/*!40000 ALTER TABLE `Animals_Medications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zookeepers`
--

DROP TABLE IF EXISTS `Zookeepers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Zookeepers` (
  `zookeeper_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  PRIMARY KEY (`zookeeper_id`),
  UNIQUE KEY `zookeeper_id` (`zookeeper_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zookeepers`
--

LOCK TABLES `Zookeepers` WRITE;
/*!40000 ALTER TABLE `Zookeepers` DISABLE KEYS */;
INSERT INTO `Zookeepers` VALUES (1,'Dottie','Duddleton'),(2,'Blanche','McDonaldson'),(3,'Ricky','Robbie'),(4,'Ricardo','Richardsington'),(5,'Zoe','Zookeeper');
/*!40000 ALTER TABLE `Zookeepers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Workdays`
--

DROP TABLE IF EXISTS `Workdays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Workdays` (
  `workday_id` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(255) NOT NULL,
  PRIMARY KEY (`workday_id`),
  UNIQUE KEY `workday_id` (`workday_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Workdays`
--

LOCK TABLES `Workdays` WRITE;
/*!40000 ALTER TABLE `Workdays` DISABLE KEYS */;
INSERT INTO `Workdays` VALUES (1,'Sunday'),(2,'Monday'),(3,'Tuesday'),(4,'Wednesday'),(5,'Thursday'),(6,'Friday'),(7,'Saturday');
/*!40000 ALTER TABLE `Workdays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zookeepers_Workdays`
--

DROP TABLE IF EXISTS `Zookeepers_Workdays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Zookeepers_Workdays` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zookeeper_id` int(11) NOT NULL,
  `workday_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `Zookeepers_Workdays_FK1` (`zookeeper_id`),
  KEY `Zookeepers_Workdays_FK2` (`workday_id`),
  CONSTRAINT `Zookeepers_Workdays_FK1` FOREIGN KEY (`zookeeper_id`) REFERENCES `Zookeepers` (`zookeeper_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Zookeepers_Workdays_FK2` FOREIGN KEY (`workday_id`) REFERENCES `Workdays` (`workday_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zookeepers_Workdays`
--

LOCK TABLES `Zookeepers_Workdays` WRITE;
/*!40000 ALTER TABLE `Zookeepers_Workdays` DISABLE KEYS */;
INSERT INTO `Zookeepers_Workdays` VALUES (1,1,2),(2,1,4),(3,1,6),(4,2,1),(5,2,2),(6,2,3),(7,2,4),(8,2,5),(9,2,6),(10,2,7);
/*!40000 ALTER TABLE `Zookeepers_Workdays` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-12 22:13:34


--------------------------------------------------------------------------------
-- The following section contains the Database Manipulation Queries for the
-- Zootopia Management System project website. All queries are included that
-- will be used for our site.
--------------------------------------------------------------------------------

-- -- -- -- -- -- -- -- Populate Tables -- -- -- -- -- -- -- -- -- -- -- -- -- -

-- Populate Animals Table:
SELECT animal_id, type, sex, name, age, weight, temperament, zookeeper_id FROM Animals;

-- Populate Medications Table:
SELECT med_id, name FROM Medications;

-- Populate Animals_Medications Table:
SELECT id, animal_id, med_id FROM Animals_Medications;

-- Populate Zookeepers Table:
SELECT zookeeper_id, first_name, last_name FROM Zookeepers;

-- Populate Workdays Table:
SELECT workday_id, day FROM Workdays;

-- Populate Zookeepers_Workdays Table:
SELECT id, zookeeper_id, workday_id FROM Zookeepers_Workdays;

-- -- -- -- -- -- -- -- Add Table Rows -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Add an Animals Row:
-- NOTE VALUE order: animal_id, type, sex, name, age, weight, temperament, zookeeper_id
INSERT INTO Animals VALUES (DEFAULT, %s, %s, %s, %s, %s, %s);

-- Add a Medications Row:
-- NOTE VALUE order: med_id, name
INSERT INTO Medications VALUES (DEFAULT, %s);

-- Add an Animals_Medications Relationship Row:
-- NOTE VALUE order: id, animal_id, med_id
INSERT INTO Animals_Medications VALUES (DEFAULT, %s, %s);

-- Add a Zookeepers Row:
-- NOTE VALUE order: zookeeper_id, first_name, last_name
INSERT INTO Zookeepers VALUES (DEFAULT, %s, %s);

-- Add a Zookeepers_Workdays Relationship Row:
-- NOTE VALUE order: id, zookeeper_id, workday_id
INSERT INTO Zookeepers_Workdays VALUES (DEFAULT, %s, %s);

-- -- -- -- -- -- -- -- Update Table Rows -- -- -- -- -- -- -- -- -- -- -- -- --

-- Update an Animal Row:
UPDATE Animals SET
    animal_id = %s,
    type = %s,
    sex = %s,
    name = %s,
    age = %s,
    weight = %s,
    temperament = %s,
    zookeeper_id = %s
    WHERE animal_id = %s

-- Update a Medications Row:
UPDATE Medications SET name = %s WHERE med_id = %s

-- Update an Animals_Medications Relationship Row:
-- NOTE: cannot simultaneously update animal_id and med_id
UPDATE Animals_Medications SET med_id = %s WHERE animal_id = %s AND med_id = %s

-- Update a Zookeepers Row:
UPDATE Zookeepers SET first_name = %s AND last_name = %s WHERE zookeeper_id= %s

-- Update a Zookeepers/Workdays Relationship Row:
UPDATE Zookeepers_Workdays SET workday_id = %s WHERE zookeeper_id = %s AND workday_id = %s

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
-- string:
SELECT * FROM Animals WHERE
    animal_id LIKE %s OR
    type LIKE %s OR
    sex LIKE %s OR
    name LIKE %s OR
    age LIKE %s OR
    weight LIKE %s OR
    temperament LIKE %s OR
    zookeeper_id LIKE %s;