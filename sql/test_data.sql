/* Test data / initial data */

INSERT INTO users(user_id, email, password_hash, admin) VALUES
    (1, "wingfrillie@gmail.com", 111, True),
    (2, "11111@caltech.edu", 111, False),
    (3, "22222@caltech.edu", 111, False),
    (4, "33333@caltech.edu", 111, False), 
    (5, "44444@caltech.edu", 111, False), 
    (6, "55555@caltech.edu", 111, False);

INSERT INTO members(user_id, last_name, first_name, preferred_name) VALUES
    (1, "Mo", "Ziyan", "Momo"), 
    (2, "Hu", "Juliette", "Julietto-sama"),
    (3, "Mo", "Ziyan", ""),
    (4, "Wu", "Helena", "Head of Heads"),
    (5, "Shao", "Eugene", "Ugne"),
    (6, "V", "Jagath", "JV");

INSERT INTO applications(user_id, application_year, school, major, gender) VALUES
    (2, 2019, "Caltech", "CS", "W"),
    (3, 2019, "MIT", "CS", "O"),
    (4, 2019, "Stanford", "CS", "W"), 
    (5, 2019, "Caltech", "CS", "M"),
    (6, 2019, "Caltech", "CS", "M");

INSERT INTO status(user_id, application_id, status) VALUES
    (2, 1, "Submitted"), 
    (3, 2, "Submitted"),
    (4, 3, "Accepted"),
    (5, 4, "RSVPed"),
    (6, 5, "Declined");
