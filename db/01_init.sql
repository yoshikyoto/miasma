CREATE DATABASE IF NOT EXISTS `miasma`;
CREATE TABLE IF NOT EXISTS `miasma`.`champion` (
  `id` int NOT NULL,
  `key` varchar(255) PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `icon_url` varchar(255)
);
