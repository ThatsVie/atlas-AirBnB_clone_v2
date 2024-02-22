-- Script that prepares a MySQL server for the project
-- database hbnb_dev_db
-- new user hbnb_dev (in localhost)
-- password of hbnb_dev set to hbnb_dev_pwd
-- hbnb_dev has all privileges on the database hbnb_dev_db only
-- hbnb_dev has SELECT privilege on the database performance_schema only
-- Doesnt fail if the database hbnb_dev_db or the user hbnb_dev already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
