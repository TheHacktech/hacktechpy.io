/*
 * This script sets up the test database for the first time.
 * It is run by Travis at the beginning of each test run.
 *
 * This script must be run by the root account.
 */

CREATE USER 'hacktech_test'@'localhost' IDENTIFIED BY 'public';
GRANT ALL PRIVILEGES ON hacktech_test.* TO 'hacktech_test'@'localhost';
