DROP TABLE IF EXISTS race;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS users;

-- Members Table
CREATE TABLE members (
    user_id            INT          NOT NULL,
    last_name          VARCHAR(255) NOT NULL,
    first_name         VARCHAR(255) NOT NULL,
    preferred_name     VARCHAR(255) DEFAULT NULL,
    middle_name        VARCHAR(255) DEFAULT NULL,
    email              VARCHAR(255) NOT NULL,
    phone              VARCHAR(64)  DEFAULT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Review Table
CREATE TABLE status (
    user_id            INT          NOT NULL,
    application_id     INT          NOT NULL,
    status             VARCHAR(50)  NOT NULL,
    decider_user_id    INT          NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (application_id) REFERENCES applications(application_id),

    PRIMARY KEY (user_id, application_id)
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
    application_year  DATETIME     DEFAULT YEAR(CURDATE()),
    school            VARCHAR(255) NOT NULL,
    major             VARCHAR(255) NOT NULL,
    degree_type       VARCHAR(50)  NOT NULL,
    graduation_year   CHAR(4)      NOT NULL,
    github            VARCHAR(255) DEFAULT NULL,
    linkedin          VARCHAR(255) DEFAULT NULL,
    resume            BLOB         NOT NULL,
    latino            BOOLEAN      DEFAULT FALSE,
    gender            CHAR(1)      NOT NULL, -- W, M, O
    shirtSize         VARCHAR(2)   NOT NULL, -- XS, S, M, L, XL
    transportation    BOOLEAN      DEFAULT FALSE,
    in_state          BOOLEAN      DEFAULT FALSE,
    bus_from          VARCHAR(50)  DEFAULT NULL,
    airport           VARCHAR(50)  DEFAULT NULL,
    diet_rest         BOOLEAN      DEFAULT FALSE,
    diet_rest_choice  VARCHAR(50)  DEFAULT NULL,
    diet_rest_detail  TEXT         DEFAULT NULL,
    q1                TEXT         DEFAULT NULL,
    q2                TEXT         DEFAULT NULL,
    q3                TEXT         DEFAULT NULL,
    q4                TEXT         DEFAULT NULL,
    codeOfConduct     BOOLEAN      DEFAULT FALSE,
    PRIMARY KEY (application_id),
    UNIQUE (user_id, application_year) -- One application per year.
);


CREATE TABLE race(
    user_id           INT,
    race_id           INT          NOT NULL AUTO_INCREMENT,
    race_type         VARCHAR(50),
    PRIMARY KEY (race_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)

-- Users Table
CREATE TABLE users (
    user_id                   INT          NOT NULL AUTO_INCREMENT,
    username                  VARCHAR(32)  NOT NULL,
    last_login                DATETIME     DEFAULT NULL,
    password_hash             VARCHAR(255) NOT NULL,
    password_reset_key        CHAR(32)     DEFAULT NULL,
    password_reset_expiration DATETIME     DEFAULT NULL,
    admin                     BOOLEAN      DEFAULT FALSE,
    PRIMARY KEY (user_id),
    UNIQUE (username)
);


