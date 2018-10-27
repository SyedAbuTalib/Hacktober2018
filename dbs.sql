-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: Hacktober18
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chattranscript`
--

DROP TABLE IF EXISTS `chattranscript`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `chattranscript` (
  `uID` int(10) NOT NULL,
  `repID` int(10) NOT NULL,
  `issueID` int(10) NOT NULL,
  `msg` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`uID`,`repID`,`issueID`),
  KEY `repID` (`repID`),
  KEY `issueID` (`issueID`),
  CONSTRAINT `chattranscript_ibfk_1` FOREIGN KEY (`uID`) REFERENCES `userinfo` (`user_id`),
  CONSTRAINT `chattranscript_ibfk_2` FOREIGN KEY (`repID`) REFERENCES `representative` (`rep_id`),
  CONSTRAINT `chattranscript_ibfk_3` FOREIGN KEY (`issueID`) REFERENCES `issue` (`issue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chattranscript`
--

LOCK TABLES `chattranscript` WRITE;
/*!40000 ALTER TABLE `chattranscript` DISABLE KEYS */;
/*!40000 ALTER TABLE `chattranscript` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Issue`
--

DROP TABLE IF EXISTS `Issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Issue` (
  `issue_id` int(10) NOT NULL,
  PRIMARY KEY (`issue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Issue`
--

LOCK TABLES `Issue` WRITE;
/*!40000 ALTER TABLE `Issue` DISABLE KEYS */;
/*!40000 ALTER TABLE `Issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repissue`
--

DROP TABLE IF EXISTS `repissue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `repissue` (
  `repID` int(10) NOT NULL,
  `uID` int(10) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`repID`,`uID`),
  KEY `uID` (`uID`),
  CONSTRAINT `repissue_ibfk_1` FOREIGN KEY (`repID`) REFERENCES `representative` (`rep_id`),
  CONSTRAINT `repissue_ibfk_2` FOREIGN KEY (`uID`) REFERENCES `userinfo` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repissue`
--

LOCK TABLES `repissue` WRITE;
/*!40000 ALTER TABLE `repissue` DISABLE KEYS */;
/*!40000 ALTER TABLE `repissue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Representative`
--

DROP TABLE IF EXISTS `Representative`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Representative` (
  `rep_id` int(10) NOT NULL,
  `rep_email` varchar(100) DEFAULT NULL,
  `rep_password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Representative`
--

LOCK TABLES `Representative` WRITE;
/*!40000 ALTER TABLE `Representative` DISABLE KEYS */;
/*!40000 ALTER TABLE `Representative` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `userdata` (
  `uID` int(10) NOT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `prev_issue_id` int(10) DEFAULT NULL,
  `region_tech_case` int(5) DEFAULT NULL,
  `region_bill_case` int(5) DEFAULT NULL,
  `common_interaction_type` varchar(50) DEFAULT NULL,
  `amnt_tech_issue` int(5) DEFAULT NULL,
  `amnt_bill_issue` int(5) DEFAULT NULL,
  `bill_amnt` double(5,2) DEFAULT NULL,
  `avg_bill_paid` double(5,2) DEFAULT NULL,
  `data_rate` int(1) DEFAULT NULL,
  `avg_speed` int(1) DEFAULT NULL,
  `intcall_request` int(3) DEFAULT NULL,
  `intcall_bool` tinyint(1) DEFAULT NULL,
  `time_between_upgrades` int(3) DEFAULT NULL,
  `device_age` int(3) DEFAULT NULL,
  `avg_call_time_five_min` int(10) DEFAULT NULL,
  `region_network_state` int(1) DEFAULT NULL,
  `failed_msg_amnt` int(5) DEFAULT NULL,
  `acnt_status` int(1) DEFAULT NULL,
  `failed_acnt_login` int(3) DEFAULT NULL,
  `amnt_disconnection_ten_min` int(2) DEFAULT NULL,
  PRIMARY KEY (`uID`),
  CONSTRAINT `userdata_ibfk_1` FOREIGN KEY (`uID`) REFERENCES `userinfo` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USERINFO`
--

DROP TABLE IF EXISTS `USERINFO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `USERINFO` (
  `user_id` int(10) NOT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `u_password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USERINFO`
--

LOCK TABLES `USERINFO` WRITE;
/*!40000 ALTER TABLE `USERINFO` DISABLE KEYS */;
/*!40000 ALTER TABLE `USERINFO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USERISSUE`
--

DROP TABLE IF EXISTS `USERISSUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `USERISSUE` (
  `uID` int(10) NOT NULL,
  `issueID` int(10) NOT NULL,
  `date` datetime DEFAULT NULL,
  `issue_status` varchar(20) DEFAULT NULL,
  `priority` int(1) DEFAULT NULL,
  PRIMARY KEY (`uID`,`issueID`),
  KEY `issueID` (`issueID`),
  CONSTRAINT `userissue_ibfk_1` FOREIGN KEY (`uID`) REFERENCES `userinfo` (`user_id`),
  CONSTRAINT `userissue_ibfk_2` FOREIGN KEY (`issueID`) REFERENCES `issue` (`issue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USERISSUE`
--

LOCK TABLES `USERISSUE` WRITE;
/*!40000 ALTER TABLE `USERISSUE` DISABLE KEYS */;
/*!40000 ALTER TABLE `USERISSUE` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-27 17:41:44
