-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 24, 2020 at 05:38 AM
-- Server version: 10.4.15-MariaDB-log
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_huberaa`
--

-- --------------------------------------------------------

--
-- Table structure for table `Animals`
--

CREATE TABLE `Animals` (
  `animal_id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `temperament` varchar(255) DEFAULT NULL,
  `zookeeper_id` int(11) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Animals`
--

INSERT INTO `Animals` (`animal_id`, `type`, `sex`, `name`, `age`, `weight`, `temperament`, `zookeeper_id`) VALUES
(1, 'Elephant', 'M', 'Hank', 34, 1299, 'Friendly', 3),
(2, 'Monkey', 'F', 'Sheryl', 10, 32, 'Lovely', 1),
(3, 'Giraffe', 'M', 'Nick', 12, 788, 'Shy', 3),
(4, 'Zebra', 'M', 'Steve', 9, 435, 'Moody', 4),
(5, 'Lion', 'M', 'Larry', 18, 575, 'Lazy', 2),
(6, 'Monkey', 'M', 'Zeus', 3, 22, 'Energetic', 1),
(7, 'Zebra', 'F', 'Sasha', 10, 770, 'Aggressive', 4),
(8, 'Elephant', 'F', 'Michelle', 32, 1089, 'Timid', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Animals_Medications`
--

CREATE TABLE `Animals_Medications` (
  `id` int(11) NOT NULL,
  `animal_id` int(11) DEFAULT NULL,
  `med_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Animals_Medications`
--

INSERT INTO `Animals_Medications` (`id`, `animal_id`, `med_id`) VALUES
(1, 1, 3),
(3, 2, 1),
(4, 2, 2),
(5, 5, 7);

-- --------------------------------------------------------

--
-- Table structure for table `Medications`
--

CREATE TABLE `Medications` (
  `med_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Medications`
--

INSERT INTO `Medications` (`med_id`, `name`) VALUES
(1, 'Penicillin'),
(2, 'Xanax'),
(3, 'Insulin'),
(4, 'Antiparasitic'),
(5, 'Steroid'),
(6, 'Opiod'),
(7, 'Catnip');

-- --------------------------------------------------------

--
-- Table structure for table `Workdays`
--

CREATE TABLE `Workdays` (
  `workday_id` int(11) NOT NULL,
  `day` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Workdays`
--

INSERT INTO `Workdays` (`workday_id`, `day`) VALUES
(1, 'Sunday'),
(2, 'Monday'),
(3, 'Tuesday'),
(4, 'Wednesday'),
(5, 'Thursday'),
(6, 'Friday'),
(7, 'Saturday');

-- --------------------------------------------------------

--
-- Table structure for table `Zookeepers`
--

CREATE TABLE `Zookeepers` (
  `zookeeper_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Zookeepers`
--

INSERT INTO `Zookeepers` (`zookeeper_id`, `first_name`, `last_name`) VALUES
(1, 'Rose', 'Nylund'),
(2, 'Blanche', 'Devereaux'),
(3, 'Cosmo', 'Kramer'),
(4, 'Jemaine', 'Clement'),
(5, 'Zoe', 'Kravitz');

-- --------------------------------------------------------

--
-- Table structure for table `Zookeepers_Workdays`
--

CREATE TABLE `Zookeepers_Workdays` (
  `id` int(11) NOT NULL,
  `zookeeper_id` int(11) NOT NULL,
  `workday_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Zookeepers_Workdays`
--

INSERT INTO `Zookeepers_Workdays` (`id`, `zookeeper_id`, `workday_id`) VALUES
(1, 1, 2),
(2, 1, 4),
(3, 1, 6),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 2, 4),
(8, 2, 5),
(9, 2, 6),
(10, 2, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Animals`
--
ALTER TABLE `Animals`
  ADD PRIMARY KEY (`animal_id`),
  ADD UNIQUE KEY `animal_id` (`animal_id`);

--
-- Indexes for table `Animals_Medications`
--
ALTER TABLE `Animals_Medications`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `Animals_Medications_FK1` (`animal_id`),
  ADD KEY `Animals_Medications_FK2` (`med_id`);

--
-- Indexes for table `Medications`
--
ALTER TABLE `Medications`
  ADD PRIMARY KEY (`med_id`),
  ADD UNIQUE KEY `med_id` (`med_id`);

--
-- Indexes for table `Workdays`
--
ALTER TABLE `Workdays`
  ADD PRIMARY KEY (`workday_id`),
  ADD UNIQUE KEY `workday_id` (`workday_id`);

--
-- Indexes for table `Zookeepers`
--
ALTER TABLE `Zookeepers`
  ADD PRIMARY KEY (`zookeeper_id`),
  ADD UNIQUE KEY `zookeeper_id` (`zookeeper_id`);

--
-- Indexes for table `Zookeepers_Workdays`
--
ALTER TABLE `Zookeepers_Workdays`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `Zookeepers_Workdays_FK1` (`zookeeper_id`),
  ADD KEY `Zookeepers_Workdays_FK2` (`workday_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Animals`
--
ALTER TABLE `Animals`
  MODIFY `animal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `Animals_Medications`
--
ALTER TABLE `Animals_Medications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Medications`
--
ALTER TABLE `Medications`
  MODIFY `med_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Workdays`
--
ALTER TABLE `Workdays`
  MODIFY `workday_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Zookeepers`
--
ALTER TABLE `Zookeepers`
  MODIFY `zookeeper_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Zookeepers_Workdays`
--
ALTER TABLE `Zookeepers_Workdays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Animals`
--
ALTER TABLE `Animals`
  ADD CONSTRAINT `Animals_FK1` FOREIGN KEY (`zookeeper_id`) REFERENCES `Zookeepers` (`zookeeper_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Animals_Medications`
--
ALTER TABLE `Animals_Medications`
  ADD CONSTRAINT `Animals_Medications_FK1` FOREIGN KEY (`animal_id`) REFERENCES `Animals` (`animal_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Animals_Medications_FK2` FOREIGN KEY (`med_id`) REFERENCES `Medications` (`med_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Zookeepers_Workdays`
--
ALTER TABLE `Zookeepers_Workdays`
  ADD CONSTRAINT `Zookeepers_Workdays_FK1` FOREIGN KEY (`zookeeper_id`) REFERENCES `Zookeepers` (`zookeeper_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Zookeepers_Workdays_FK2` FOREIGN KEY (`workday_id`) REFERENCES `Workdays` (`workday_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
