DROP DATABASE IF EXISTS `portfolio_richardinfo`;
CREATE DATABASE `portfolio_richardinfo`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
GRANT ALL PRIVILEGES ON portfolio_richardinfo.* TO 'root'@'localhost' IDENTIFIED BY ''

WITH GRANT OPTION;
FLUSH PRIVILEGES;
