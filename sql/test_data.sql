/* Test data / initial data */

INSERT INTO members(uid, last_name, first_name, email, phone) VALUES
    ('1957540', 'Qu', 'David', 'davidqu12345@gmail.com', NULL),
    ('1984853', 'Eng', 'Robert', 'reng@caltech.edu', '+11234567890');

INSERT INTO members(
    user_id,
    uid,
    last_name,
    first_name,
    preferred_name,
    middle_name,
    email,
    phone,
    gender,
    gender_custom,
    birthday,
    entry_year,
    graduation_year,
    msc,
    city,
    state,
    building_id,
    room
) VALUES (
    3,
    '2078141',
    'Sander',
    'Caleb',
    'Cleb',
    'Caldwell',
    'csander@caltech.edu',
    '6178003347',
    0,
    'Male',
    '1999-05-08',
    2017,
    2021,
    707,
    'Lincoln',
    'MA',
    1,
    '203'
);

INSERT INTO users(user_id, username) VALUES
    (1, "dqu"),
    (2, "reng"),
    (3, "csander"),
    (4, "ruddock_pres");
