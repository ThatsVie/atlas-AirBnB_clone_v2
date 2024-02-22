-- Script that prepares a MySQL server for the project
-- database hbnb_test_db
-- new user hbnb_test (in localhost)
-- password of hbnb_test set to hbnb_test_pwd
-- hbnb_test has all privileges on the database hbnb_test_db only
-- hbnb_test has SELECT privilege on the database performance_schema only
-- Doesn't fail if database hbnb_test_db or user hbnb_test already exists

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
