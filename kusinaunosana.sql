-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2024 at 04:33 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kusinaunosana`
--

-- --------------------------------------------------------

--
-- Table structure for table `reservations`
--

CREATE TABLE `reservations` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `area` varchar(255) NOT NULL,
  `pax` int(11) NOT NULL,
  `time` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `payment_method` varchar(255) NOT NULL,
  `total_price` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reservations`
--

INSERT INTO `reservations` (`id`, `name`, `email`, `contact`, `area`, `pax`, `time`, `date`, `payment_method`, `total_price`) VALUES
(3, 'lady-anne pulido', 'lady@gmail.com', '2384366345', 'Inside Dining', 1, 'BREAKFAST (7:00 AM-10:59 AM)', '2024-05-19', 'Credit Card', '700.00'),
(4, 'Jhuncel Adan', 'jhuncel2@gmail.com', '09124817641', 'Inside Dining', 10, 'BREAKFAST (7:00 AM-10:59 AM)', '2024-05-19', 'PayPal', '2500.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
