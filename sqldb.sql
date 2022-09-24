/*
SQLyog Ultimate v10.00 Beta1
MySQL - 5.5.5-10.4.24-MariaDB : Database - readreview
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`readreview` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `readreview`;

/*Table structure for table `newbook` */

DROP TABLE IF EXISTS `newbook`;

CREATE TABLE `newbook` (
  `BookId` INT(11) NOT NULL AUTO_INCREMENT,
  `BookName` VARCHAR(50) DEFAULT NULL,
  `AuthorName` VARCHAR(50) DEFAULT NULL,
  `PublisherName` VARCHAR(50) DEFAULT NULL,
  `PublishedYear` VARCHAR(10) DEFAULT NULL,
  `Image` VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (`BookId`)
) ENGINE=INNODB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `newbook` */

INSERT  INTO `newbook`(`BookId`,`BookName`,`AuthorName`,`PublisherName`,`PublishedYear`,`Image`) 
VALUES (6,'C Language','Dennis','penguine books','2020','Pic6.jpg'),
(9,'Verity','Collen Hoover','Sapna book house ','2018','Reminders of him.jpg'),
(10,'Reminders of him','Collen Hoover','Sapna book house ','2022','verity.jpg'),
(8,'C++','Jbaurne','Subhash','2022','C++.jpg');

/*Table structure for table `newreview` */

DROP TABLE IF EXISTS `newreview`;

CREATE TABLE `newreview` (
  `ReviewId` INT(11) NOT NULL AUTO_INCREMENT,
  `UserId` INT(11) DEFAULT NULL,
  `FirstName` VARCHAR(50) DEFAULT NULL,
  `LastName` VARCHAR(50) DEFAULT NULL,
  `EmailId` VARCHAR(50) DEFAULT NULL,
  `PhoneNumber` VARCHAR(20) DEFAULT NULL,
  `BookId` INT(11) DEFAULT NULL,
  `BookName` VARCHAR(50) DEFAULT NULL,
  `AuthorName` VARCHAR(50) DEFAULT NULL,
  `PublisherName` VARCHAR(50) DEFAULT NULL,
  `PublishedYear` VARCHAR(10) DEFAULT NULL,
  `Rating` VARCHAR(10) DEFAULT NULL,
  `Comments` VARCHAR(250) DEFAULT NULL,
  PRIMARY KEY (`ReviewId`)
) ENGINE=INNODB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `newreview` */

INSERT  INTO `newreview`(`ReviewId`,`UserId`,`FirstName`,`LastName`,`EmailId`,`PhoneNumber`,`BookId`,`BookName`,`AuthorName`,`PublisherName`,`PublishedYear`,`Rating`,`Comments`) 
VALUES (1,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','5',NULL),
(2,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','4',NULL),
(3,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','3','nice'),
(4,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','5',NULL),
(5,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','2','average'),
(6,1,'aaa','aaa','aa@gmail.com','9886239083',6,'C Language','Dennis','Subhash','2022','1','nice'),
(7,1,'aaa','aaa','aa@gmail.com','9886239083',8,'C++','Jbaurne','Subhash','2022','5','good');

/*Table structure for table `newuser` */

DROP TABLE IF EXISTS `newuser`;

CREATE TABLE `newuser` (
  `UserId` INT(11) NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(50) DEFAULT NULL,
  `LastName` VARCHAR(50) DEFAULT NULL,
  `UserName` VARCHAR(50) DEFAULT NULL,
  `Password` VARCHAR(50) DEFAULT NULL,
  `EmailId` VARCHAR(50) DEFAULT NULL,
  `PhoneNumber` VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=INNODB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `newuser` */

INSERT  INTO `newuser`(`UserId`,`FirstName`,`LastName`,`UserName`,`Password`,`EmailId`,`PhoneNumber`) 
VALUES (1,'harshitha','gr','harshitha','12345','harshitha@gmail.com','9886239083'),
(2,'Soundarya','S','soundarya','1234','soundarya@gmail.com','9234633644');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
