/* Test data / initial data */

INSERT INTO users(user_id, email, password_hash, admin) VALUES
    (1, "wingfrillie@gmail.com", 111, True),
    (2, "1", 111, False),
    (3, "2", 111, False),
    (4, "3", 111, False), 
    (5, "4", 111, False), 
    (6, "5", 111, False);

INSERT INTO members(user_id, last_name, first_name, preferred_name, date_of_birth) VALUES
    (1, "Mo", "Ziyan", "Momo", NOW()), 
    (2, "Hu", "Juliette", "Julietto-sama", NOW()),
    (3, "Mo", "Ziyan", "", NOW()),
    (4, "Wu", "Helena", "Head of Heads", NOW()),
    (5, "Shao", "Eugene", "Ugne", NOW()),
    (6, "V", "Jagath", "JV", NOW());

INSERT INTO applications(user_id, application_year, school, major, gender) VALUES
    (2, NOW(), "Caltech", "CS", "W"),
    (3, NOW(), "MIT", "CS", "O"),
    (4, NOW(), "Stanford", "CS", "W"), 
    (5, NOW(), "Caltech", "CS", "M"),
    (6, NOW(), "Caltech", "CS", "M");

INSERT INTO status(user_id, application_id, status) VALUES
    (2, 1, "Submitted"), 
    (3, 2, "Submitted"),
    (4, 3, "Accepted"),
    (5, 4, "RSVPed"),
    (6, 5, "Declined");
