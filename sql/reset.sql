/*
 * This script resets the test database to a consistent state
 * and should be run at the beginning of each integration test.
 */

DROP DATABASE IF EXISTS hacktech_test;
CREATE DATABASE hacktech_test;
USE hacktech_test;

-- Create the database schema.
SOURCE sql/hacktech.sql

-- Populate with test data.
SOURCE sql/test_data.sql
