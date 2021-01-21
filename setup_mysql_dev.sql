-- MySQL setup development 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_deve'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_deve'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_deve'@'localhost';
