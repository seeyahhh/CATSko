CREATE DATABASE  IF NOT EXISTS `catsko` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `catsko`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: catsko
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `applicant`
--

DROP TABLE IF EXISTS `applicant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applicant` (
  `App_ID` int NOT NULL AUTO_INCREMENT,
  `App_Name` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Temp_Address` varchar(255) NOT NULL,
  `Town` varchar(100) NOT NULL,
  `Zip` varchar(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `H_Phone` varchar(20) DEFAULT NULL,
  `C_Phone` varchar(20) NOT NULL,
  `M_Address` varchar(255) DEFAULT NULL,
  `S_Name` varchar(100) DEFAULT NULL,
  `Living_Arr` enum('Rent','Own Home','Live with Owner') NOT NULL,
  `Home_Type` enum('House','Condo','Duplex','Mobile/Land','Mobile in Park') DEFAULT NULL,
  `Know_Pet` tinyint(1) DEFAULT NULL,
  `Rent_Type` enum('House','Condo','Duplex','Mobile Home','Dorm') DEFAULT NULL,
  `Landlord_Name` varchar(100) DEFAULT NULL,
  `Landlord_Phone` varchar(20) DEFAULT NULL,
  `Vet_Name` varchar(100) NOT NULL,
  `Allergies` tinyint(1) NOT NULL,
  `Shel_History` tinyint(1) NOT NULL,
  `In_Out` enum('Indoor Only','Indoor/Outdoor') NOT NULL,
  `Declaw` tinyint(1) NOT NULL,
  `Child_Count` int DEFAULT NULL,
  `Child_Age` int DEFAULT NULL,
  PRIMARY KEY (`App_ID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `C_Phone_UNIQUE` (`C_Phone`),
  KEY `idx_applicant_name` (`App_Name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applicant`
--

LOCK TABLES `applicant` WRITE;
/*!40000 ALTER TABLE `applicant` DISABLE KEYS */;
INSERT INTO `applicant` VALUES (1,'Ayse Catampatan','2005-10-17','Manila','Manila','1060','aysemcatampatan@gmail.com',NULL,'09293439201','Tanay',NULL,'Rent',NULL,NULL,'Dorm','Vicente Cruz','09912345678','Tanay Vet Clinic',0,1,'Indoor/Outdoor',0,2,2),(2,'Jeter D. Dela Rosa','2004-11-27','Manila','Manila','1060','jeterdr@gmail.com',NULL,'09123123123','Batangas','Lorena Sanchez','Live with Owner',NULL,1,NULL,NULL,NULL,'Bacood Veterinary',0,0,'Indoor/Outdoor',0,NULL,NULL),(3,'Josh Oliver','2004-12-03','Manila','Manila','1060','josholi@gmail.com',NULL,'09456456456',NULL,NULL,'Live with Owner',NULL,NULL,NULL,NULL,NULL,'Sta.Mesa Vet',0,1,'Indoor Only',0,1,0),(4,'Avril Saliba','2004-04-04','Manila','Manila','1060','avrils@gmail.com',NULL,'09789789789','Bulacan','Angelica Pastrana','Own Home','Condo',NULL,NULL,NULL,NULL,'Bulacan Vet Clinic',0,0,'Indoor Only',1,0,0),(5,'Chauncey Umali','2004-08-14','Antipolo','Rizal','1870','chaofan@gmail.com',NULL,'09246246246','',NULL,'Live with Owner',NULL,0,NULL,NULL,NULL,'Antipolo Veterinary',1,0,'Indoor/Outdoor',1,NULL,NULL),(6,'Gwen Lee','2004-12-09','Sta.Mesa','Manila','1060','glee@gmail.com',NULL,'09369369369','Cavite',NULL,'Own Home','Condo',NULL,NULL,NULL,NULL,'Cavite Vet',1,1,'Indoor Only',1,0,NULL),(7,'Dinon Isaig','2004-10-04','Taguig','Taguig','1208','deenawn@gmail.com',NULL,'09484848484',NULL,NULL,'Live with Owner',NULL,1,NULL,NULL,NULL,'Taguic Veterinary',0,0,'Indoor/Outdoor',0,0,NULL),(8,'Mary Lois Denosta','2004-04-14','Quezon City','Quezon City','1101','biniluwi@gmail.com',NULL,'09129129129',NULL,NULL,'Live with Owner',NULL,1,NULL,NULL,NULL,'QC Animal Clinic',1,0,'Indoor Only',0,NULL,NULL),(9,'Gianne Dasco','2003-01-20','Paranaque','Paranaque','1019','gigi@gmail.com',NULL,'09843843843','Bicol',NULL,'Live with Owner',NULL,0,NULL,NULL,NULL,'Bicol Pet Clinic',1,1,'Indoor Only',1,NULL,NULL),(10,'Joshua Tanawan','2005-04-28','Sta.Mesa','Manila','1016','joshwae@gmail.com',NULL,'09523523523','Morong','Kristan','Rent',NULL,NULL,'Condo','Claire Esmeralda','09721721721','Morong Vet',0,1,'Indoor/Outdoor',1,3,1);
/*!40000 ALTER TABLE `applicant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pet`
--

DROP TABLE IF EXISTS `pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet` (
  `App_ID` int NOT NULL,
  `P_ID` int NOT NULL,
  `P_Name` varchar(100) NOT NULL,
  `P_Breed` varchar(100) NOT NULL,
  `P_Age` int NOT NULL,
  `P_Sex` enum('M','F') NOT NULL,
  `Spay_Neut` tinyint(1) NOT NULL,
  `St_Own` tinyint(1) NOT NULL,
  `Kept_where` varchar(255) NOT NULL,
  `P_Happened` text,
  PRIMARY KEY (`App_ID`,`P_ID`),
  CONSTRAINT `pet_ibfk_1` FOREIGN KEY (`App_ID`) REFERENCES `applicant` (`App_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet`
--

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
INSERT INTO `pet` VALUES (1,1,'Potchi','Shih Tzu',4,'F',0,1,'Living Room','Still with applicant'),(1,2,'Milo','Maltese',3,'M',0,1,'Living Room','Still with applicant'),(1,3,'Lemon','Burmese',2,'M',0,0,'Outdoors','Deceased'),(2,1,'Max','Burmese',5,'F',0,1,'Living Room','Still with applicant'),(3,1,'Jatak','Scottish Fold',1,'F',0,1,'House','Still with Applicant'),(3,2,'Ming','British Shorthair',10,'M',1,0,'Cage','Died of old age'),(4,1,'Chai','Siamese',5,'F',1,1,'House',NULL),(6,1,'Princess','Persian Cat',3,'F',1,1,'House','Still with Applicant'),(6,2,'Non','Siamese',6,'M',1,1,'House',NULL),(8,1,'Icy','Persian Cat',5,'F',1,0,'House','Deceased');
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'catsko'
--

--
-- Dumping routines for database 'catsko'
--
/*!50003 DROP PROCEDURE IF EXISTS `delete_applicant` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_applicant`(
  IN a_id INT
)
BEGIN
  DELETE FROM Applicant
  WHERE App_ID = a_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_pet` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_pet`(
  IN p_app_id INT,
  IN p_id INT
)
BEGIN
  DELETE FROM Pet
  WHERE App_ID = p_app_id AND P_ID = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_applicants_by_declaw` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_applicants_by_declaw`()
BEGIN
  SELECT Declaw,
    GROUP_CONCAT(App_Name SEPARATOR ', ') AS Applicants
  FROM Applicant
  GROUP BY Declaw;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_applicants_without_pets` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_applicants_without_pets`()
BEGIN
  SELECT 
    a.App_ID, a.App_Name
  FROM Applicant a
  LEFT JOIN Pet p ON a.App_ID = p.App_ID
  WHERE p.App_ID IS NULL;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_applicant_count_by_living_arr` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_applicant_count_by_living_arr`()
BEGIN
  SELECT Living_Arr, COUNT(*) AS Count_Living
  FROM Applicant
  GROUP BY Living_Arr
  HAVING COUNT(*) >= 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_pet_applicant_join` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_pet_applicant_join`()
BEGIN
  SELECT 
    a.App_ID, a.App_Name, a.Town,
    p.P_ID, p.P_Name, p.P_Breed
  FROM Applicant a
  JOIN Pet p ON a.App_ID = p.App_ID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_pet_count_by_town` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_pet_count_by_town`()
BEGIN
  SELECT 
    a.Town,
    COUNT(p.P_ID) AS Total_Pets
  FROM Applicant a
  JOIN Pet p ON a.App_ID = p.App_ID
  GROUP BY a.Town;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_spayed_neutered_pet_count` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_spayed_neutered_pet_count`()
BEGIN
  SELECT 
    COUNT(*) AS Spayed_Neutered_Count
  FROM Pet
  WHERE Spay_Neut = TRUE;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_applicant` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_applicant`(
  IN a_name VARCHAR(100),
  IN dob DATE,
  IN temp_addr VARCHAR(255),
  IN town VARCHAR(100),
  IN zip VARCHAR(10),
  IN email VARCHAR(100),
  IN h_phone VARCHAR(20),
  IN c_phone VARCHAR(20),
  IN m_addr VARCHAR(255),
  IN s_name VARCHAR(100),
  IN living_arr ENUM('Rent', 'Own Home', 'Live with Owner'),
  IN home_type ENUM('House', 'Condo', 'Duplex', 'Mobile/Land', 'Mobile in Park'),
  IN know_pet BOOLEAN,
  IN rent_type ENUM('House', 'Condo', 'Duplex', 'Mobile Home', 'Dorm'),
  IN landlord_name VARCHAR(100),
  IN landlord_phone VARCHAR(20),
  IN vet_name VARCHAR(100),
  IN allergies BOOLEAN,
  IN shel_history BOOLEAN,
  IN in_out ENUM('Indoor Only', 'Indoor/Outdoor'),
  IN declaw BOOLEAN,
  IN child_count INT,
  IN child_age INT
)
BEGIN
  INSERT INTO Applicant (
    App_Name, DOB, Temp_Address, Town, Zip, Email, H_Phone, C_Phone, M_Address,
    S_Name, Living_Arr, Home_Type, Know_Pet, Rent_Type, Landlord_Name,
    Landlord_Phone, Vet_Name, Allergies, Shel_History, In_Out, Declaw,
    Child_Count, Child_Age
  ) VALUES (
    a_name, dob, temp_addr, town, zip, email, h_phone, c_phone, m_addr,
    s_name, living_arr, home_type, know_pet, rent_type, landlord_name,
    landlord_phone, vet_name, allergies, shel_history, in_out, declaw,
    child_count, child_age
  );
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_pet_per_applicant` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_pet_per_applicant`(
  IN p_app_id INT,
  IN p_name VARCHAR(100),
  IN p_breed VARCHAR(100),
  IN p_age INT,
  IN p_sex ENUM('M','F'),
  IN p_spay_neut BOOLEAN,
  IN p_st_own BOOLEAN,
  IN p_kept_where VARCHAR(255),
  IN p_happened TEXT
)
BEGIN
  DECLARE next_pet_id INT;

  SELECT IFNULL(MAX(P_ID), 0) + 1 INTO next_pet_id
  FROM Pet
  WHERE App_ID = p_app_id;

  INSERT INTO Pet (
    App_ID, P_ID, P_Name, P_Breed, P_Age, P_Sex,
    Spay_Neut, St_Own, Kept_where, P_Happened
  )
  VALUES (
    p_app_id, next_pet_id, p_name, p_breed, p_age, p_sex,
    p_spay_neut, p_st_own, p_kept_where, p_happened
  );
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `pet_count_by_breed` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `pet_count_by_breed`()
BEGIN
  SELECT UPPER(P_Breed) AS "Pet Breed", COUNT(*) AS "Pet Count"
  FROM Pet
  GROUP BY UPPER(P_Breed);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `search_applicant_by_name` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `search_applicant_by_name`(
  IN search_name VARCHAR(100)
)
BEGIN
  SELECT * FROM Applicant
  WHERE LOWER(App_Name) LIKE CONCAT('%', LOWER(search_name), '%');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `search_by_appid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `search_by_appid`(IN search_id INT)
BEGIN
  SELECT * 
  FROM Applicant
  WHERE App_ID = search_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sort_appname` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sort_appname`()
BEGIN
  SELECT *
  FROM Applicant
  ORDER BY App_Name ASC;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_applicant` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_applicant`(
  IN a_id INT,
  IN a_name VARCHAR(100),
  IN dob DATE,
  IN temp_addr VARCHAR(255),
  IN town VARCHAR(100),
  IN zip VARCHAR(10),
  IN email VARCHAR(100),
  IN h_phone VARCHAR(20),
  IN c_phone VARCHAR(20),
  IN m_addr VARCHAR(255),
  IN s_name VARCHAR(100)
)
BEGIN
  UPDATE Applicant
  SET App_Name = a_name,
      DOB = dob,
      Temp_Address = temp_addr,
      Town = town,
      Zip = zip,
      Email = email,
      H_Phone = h_phone,
      C_Phone = c_phone,
      M_Address = m_addr,
      S_Name = s_name
  WHERE App_ID = a_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_pet` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_pet`(
  IN p_app_id INT,
  IN p_id INT,
  IN p_name VARCHAR(100),
  IN p_breed VARCHAR(100),
  IN p_age INT,
  IN p_sex ENUM('M','F'),
  IN p_spay_neut BOOLEAN,
  IN p_st_own BOOLEAN,
  IN p_kept_where VARCHAR(255),
  IN p_happened TEXT
)
BEGIN
  UPDATE Pet
  SET P_Name = p_name,
      P_Breed = p_breed,
      P_Age = p_age,
      P_Sex = p_sex,
      Spay_Neut = p_spay_neut,
      St_Own = p_st_own,
      Kept_where = p_kept_where,
      P_Happened = p_happened
  WHERE App_ID = p_app_id AND P_ID = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-19 11:48:02
