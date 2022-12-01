-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2022 at 05:53 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `security`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `cursor_1` ()   BEGIN
      DECLARE done INT DEFAULT 0;
      DECLARE A,B,C,D,E,F,G,H VARCHAR(30);
      DECLARE cur CURSOR FOR SELECT * FROM resident;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
      OPEN cur;
      label: LOOP
      FETCH cur INTO A,B,C,D,E,F;
      INSERT INTO resident_backup VALUES(A,B,C,D,E,F);
      IF done = 1 THEN LEAVE label;
      END IF;
      END LOOP;
      CLOSE cur;
   END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `RESIDENTS_INFO` (IN `X` INT)   BEGIN
    SELECT * FROM resident WHERE resident_id = X;
    END$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `tenancy` (`Allocated` INT) RETURNS VARCHAR(100) CHARSET utf8mb4 DETERMINISTIC BEGIN
    if Allocated>10 THEN
    	RETURN ('No more houses left');
    ELSE
    	RETURN ('There is vacancy');
    END if;
    END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `block`
--

CREATE TABLE `block` (
  `block_id` int(10) NOT NULL,
  `block_name` varchar(255) NOT NULL,
  `residents` varchar(255) DEFAULT NULL,
  `houses` int(11) DEFAULT NULL,
  `visitors` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `block`
--

INSERT INTO `block` (`block_id`, `block_name`, `residents`, `houses`, `visitors`) VALUES
(1, 'A Block', '1', 50, NULL),
(2, 'B Block', '1', 52, NULL),
(3, 'C Block', '1', 45, NULL),
(4, 'D Block', '1', 40, NULL),
(5, 'E Block', '1', 55, NULL),
(6, 'F Block', '1', 50, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `house`
--

CREATE TABLE `house` (
  `house_id` int(10) NOT NULL,
  `block_id` int(10) NOT NULL,
  `house_no` int(10) NOT NULL,
  `Allocated` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `house`
--

INSERT INTO `house` (`house_id`, `block_id`, `house_no`, `Allocated`) VALUES
(1, 1, 10, 1),
(2, 2, 10, 1),
(3, 3, 10, 1),
(4, 4, 10, 1),
(5, 5, 10, 10),
(6, 6, 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE `resident` (
  `resident_id` varchar(255) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Mob_no` varchar(255) NOT NULL,
  `block_id` int(10) DEFAULT NULL,
  `house_id` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`resident_id`, `Fname`, `Lname`, `Mob_no`, `block_id`, `house_id`) VALUES
('250', 'Sunny', 'Singh', '9873214560', 1, 1),
('251', 'Karan', 'Gupta', '7337265192', 2, 2),
('252', 'Ankit', 'Tiwari', '6937265192', 3, 3),
('253', 'Prakash', 'Kumar', '9637265192', 4, 4),
('254', 'Naveen', 'Kumar', '6397265192', 5, 5),
('255', 'Sandy', 'Naik', '9667265192', 6, 6);

--
-- Triggers `resident`
--
DELIMITER $$
CREATE TRIGGER `resident_insertion` BEFORE INSERT ON `resident` FOR EACH ROW BEGIN
DECLARE error_msg VARCHAR(255);
SET error_msg = ('Cannot allocate more tenancy');
IF (New.resident_id ) > 255
THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg; 
END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `resident_backup`
--

CREATE TABLE `resident_backup` (
  `resident_id` varchar(6) DEFAULT NULL,
  `Fname` varchar(30) DEFAULT NULL,
  `LNAME` varchar(16) DEFAULT NULL,
  `Mob_no` varchar(10) DEFAULT NULL,
  `block_id` varchar(6) DEFAULT NULL,
  `house_id` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resident_backup`
--

INSERT INTO `resident_backup` (`resident_id`, `Fname`, `LNAME`, `Mob_no`, `block_id`, `house_id`) VALUES
('250', 'Sunny', 'Singh', '9873214560', '1', '1'),
('251', 'Karan', 'Gupta', '7337265192', '2', '2'),
('252', 'Ankit', 'Tiwari', '6937265192', '3', '3'),
('253', 'Prakash', 'Kumar', '9637265192', '4', '4'),
('254', 'Naveen', 'Kumar', '6397265192', '5', '5'),
('255', 'Sandy', 'Naik', '9667265192', '6', '6'),
('255', 'Sandy', 'Naik', '9667265192', '6', '6');

-- --------------------------------------------------------

--
-- Table structure for table `security_manager`
--

CREATE TABLE `security_manager` (
  `manager_id` int(10) NOT NULL,
  `username` varchar(255) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Mob_no` varchar(255) NOT NULL,
  `block_id` int(10) NOT NULL,
  `password` longtext NOT NULL,
  `is_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `security_manager`
--

INSERT INTO `security_manager` (`manager_id`, `username`, `Fname`, `Lname`, `Mob_no`, `block_id`, `password`, `is_admin`) VALUES
(1, 'manager1', 'Ankush', 'Singh', '9871234560', 1, 'password1', 0),
(2, 'manager2', 'Raj', 'Naik', '9813234560', 2, 'password2', 0),
(3, 'manager3', 'Varum', 'Mahale', '9845634560', 3, 'password3', 0),
(4, 'manager4', 'Arun', 'Singh', '9789234560', 4, 'password4', 0),
(5, 'manager5', 'Sandeep', 'Kumar', '9852634560', 5, 'password5', 0),
(6, 'manager7', 'Arjun', 'Singh', '9963234560', 5, 'password6', 0);

-- --------------------------------------------------------

--
-- Table structure for table `visitor`
--

CREATE TABLE `visitor` (
  `visitor_id` int(11) NOT NULL,
  `in_time` datetime DEFAULT NULL,
  `out_time` datetime DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `resident_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `visitor`
--

INSERT INTO `visitor` (`visitor_id`, `in_time`, `out_time`, `name`, `resident_id`) VALUES
(661, '2022-06-18 10:34:09', '2022-06-18 11:34:09', 'Vivek Kumar', '252');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `block`
--
ALTER TABLE `block`
  ADD PRIMARY KEY (`block_id`);

--
-- Indexes for table `house`
--
ALTER TABLE `house`
  ADD PRIMARY KEY (`house_id`),
  ADD KEY `block_id` (`block_id`);

--
-- Indexes for table `resident`
--
ALTER TABLE `resident`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `block_id` (`block_id`),
  ADD KEY `house_id` (`house_id`);

--
-- Indexes for table `security_manager`
--
ALTER TABLE `security_manager`
  ADD PRIMARY KEY (`manager_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `block_id` (`block_id`);

--
-- Indexes for table `visitor`
--
ALTER TABLE `visitor`
  ADD PRIMARY KEY (`visitor_id`),
  ADD KEY `resident_id` (`resident_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `block`
--
ALTER TABLE `block`
  MODIFY `block_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `house`
--
ALTER TABLE `house`
  MODIFY `house_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `security_manager`
--
ALTER TABLE `security_manager`
  MODIFY `manager_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `house`
--
ALTER TABLE `house`
  ADD CONSTRAINT `house_ibfk_1` FOREIGN KEY (`block_id`) REFERENCES `block` (`block_id`);

--
-- Constraints for table `resident`
--
ALTER TABLE `resident`
  ADD CONSTRAINT `resident_ibfk_1` FOREIGN KEY (`block_id`) REFERENCES `block` (`block_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `resident_ibfk_2` FOREIGN KEY (`house_id`) REFERENCES `house` (`house_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `security_manager`
--
ALTER TABLE `security_manager`
  ADD CONSTRAINT `security_manager_ibfk_1` FOREIGN KEY (`block_id`) REFERENCES `block` (`block_id`);

--
-- Constraints for table `visitor`
--
ALTER TABLE `visitor`
  ADD CONSTRAINT `visitor_ibfk_1` FOREIGN KEY (`resident_id`) REFERENCES `resident` (`resident_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
