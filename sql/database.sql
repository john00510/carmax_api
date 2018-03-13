DROP DATABASE IF EXISTS cars;
CREATE DATABASE cars;
CREATE USER 'cars'@'localhost' IDENTIFIED BY 'cars';
GRANT ALL PRIVILEGES ON cars.* TO 'cars'@'localhost';

