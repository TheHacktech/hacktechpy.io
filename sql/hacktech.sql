DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS members;

-- Members Table
CREATE TABLE members (
    user_id            INT          NOT NULL AUTO_INCREMENT,
    last_name          VARCHAR(255) NOT NULL,
    first_name         VARCHAR(255) NOT NULL,
    preferred_name     VARCHAR(255) DEFAULT NULL,
    middle_name        VARCHAR(255) DEFAULT NULL,
    email              VARCHAR(255) NOT NULL,
    phone              VARCHAR(64)  DEFAULT NULL,
    gender_custom      CHAR(1)  DEFAULT NULL, -- W, M, O
    address            VARCHAR(255) DEFAULT NULL,
    city               VARCHAR(64)  DEFAULT NULL,
    state              VARCHAR(64)  DEFAULT NULL,
    zip                VARCHAR(9)   DEFAULT NULL,
    country            VARCHAR(64)  DEFAULT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (building_id) REFERENCES buildings(building_id),
    UNIQUE (uid)
);

-- Member Full Name View
CREATE VIEW members_full_name AS (
    SELECT user_id,
        CONCAT(IFNULL(preferred_name, first_name), ' ', last_name) AS full_name
    FROM members
);

-- Users Table
CREATE TABLE users (
    user_id                   INT,
    username                  VARCHAR(32)  NOT NULL,
    last_login                DATETIME     DEFAULT NULL,
    password_hash             VARCHAR(255) NOT NULL,
    password_reset_key        CHAR(32)     DEFAULT NULL,
    password_reset_expiration DATETIME     DEFAULT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES members(user_id),
    UNIQUE (username)
);
