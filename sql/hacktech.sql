DROP TABLE IF EXISTS race;
DROP VIEW IF EXISTS members_full_name;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS users;

-- Users Table
CREATE TABLE users (
    user_id                   INT          NOT NULL AUTO_INCREMENT,
    email                     VARCHAR(255) NOT NULL,
    last_login                DATETIME     DEFAULT NULL,
    password_hash             VARCHAR(255) NOT NULL,
    password_reset_key        CHAR(32)     DEFAULT NULL,
    password_reset_expiration DATETIME     DEFAULT NULL,
    activated                 BOOLEAN      DEFAULT FALSE,
    confirm_account_key       CHAR(32)     DEFAULT NULL,
    admin                     BOOLEAN      DEFAULT FALSE,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

-- Members Table
CREATE TABLE members (
    user_id            INT          NOT NULL,
    first_name         VARCHAR(255) NOT NULL,
    preferred_name     VARCHAR(255) DEFAULT NULL,
    middle_name        VARCHAR(255) DEFAULT NULL,
    last_name          VARCHAR(255) NOT NULL,
    date_of_birth      DATE NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Member Full Name View
CREATE VIEW members_full_name AS (
    SELECT user_id,
        CONCAT(IFNULL(preferred_name, first_name), ' ', last_name) AS full_name
    FROM members
);

CREATE TABLE applications(
    application_id    INT          NOT NULL AUTO_INCREMENT,
    user_id           INT          NOT NULL,
    application_year  DATETIME     DEFAULT NULL,
    phone             VARCHAR(64)  DEFAULT NULL,
    school            VARCHAR(255) DEFAULT NULL,
    major             VARCHAR(255) DEFAULT NULL,
    degree_type       VARCHAR(50)  DEFAULT NULL,
    graduation_year   CHAR(4)      DEFAULT NULL,
    github            VARCHAR(255) DEFAULT NULL,
    linkedin          VARCHAR(255) DEFAULT NULL,
    resume            BLOB         DEFAULT NULL,
    latino            BOOLEAN      DEFAULT FALSE,
    gender            CHAR(1)      DEFAULT NULL, -- W, M, O
    shirt_size        VARCHAR(2)  DEFAULT NULL, -- XS, S, M, L, XL
    transportation    BOOLEAN      DEFAULT FALSE,
    in_state          BOOLEAN      DEFAULT FALSE,
    bus_from          VARCHAR(50)  DEFAULT NULL,
    airport           VARCHAR(50)  DEFAULT NULL,
    diet_rest         BOOLEAN      DEFAULT FALSE,
    diet_rest_detail  TEXT         DEFAULT NULL,
    q1                TEXT         DEFAULT NULL,
    q2                TEXT         DEFAULT NULL,
    q3                TEXT         DEFAULT NULL,
    q4                TEXT         DEFAULT NULL,
    code_of_conduct     BOOLEAN    DEFAULT FALSE,
    PRIMARY KEY (application_id),
    UNIQUE (user_id, application_year) -- One application per year.
);

-- Review Table
CREATE TABLE status(
    user_id            INT          NOT NULL,
    application_id     INT          NOT NULL,
    status             VARCHAR(50)  NOT NULL,
    decider_user_id    INT          DEFAULT NULL,
    reimbursement_amt  INT	    DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (application_id) REFERENCES applications(application_id),
    PRIMARY KEY (user_id, application_id)
);


CREATE TABLE diet(
    user_id           INT,
    diet_id           INT    NOT NULL AUTO_INCREMENT,
    diet_restrictions        VARCHAR(50),
    PRIMARY KEY (diet_id),
    UNIQUE(user_id, diet_restrictions),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE race(
    user_id           INT,
    race_id           INT          NOT NULL AUTO_INCREMENT,
    race_type         VARCHAR(50),
    PRIMARY KEY (race_id),
    UNIQUE(user_id, race_type),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

