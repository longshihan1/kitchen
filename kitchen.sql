/*
 Navicat Premium Data Transfer

 Source Server         : 自己的
 Source Server Type    : MySQL
 Source Server Version : 50710
 Source Host           : localhost:3306
 Source Schema         : kitchen

 Target Server Type    : MySQL
 Target Server Version : 50710
 File Encoding         : 65001

 Date: 13/12/2018 21:50:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for kitchen
-- ----------------------------
DROP TABLE IF EXISTS `kitchen`;
CREATE TABLE `kitchen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `topimg` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `cookcount` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `author_img` varchar(255) DEFAULT NULL,
  `desmessage` text,
  `imgsmessage` text,
  `stepsmessage` text,
  `tip` text,
  `videourl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
