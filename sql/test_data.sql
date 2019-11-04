/* Test data / initial data */

INSERT INTO users(user_id, email, password_hash, admin) VALUES
    (1, "zmo@yahoo.com", 111, True),
    (2, "jmu@caltech.edu", 111, False),
    (3, "zo@caltech.edu", 111, False),
    (4, "hwu@caltech.edu", 111, False), 
    (5, "ugne@caltech.edu", 111, False), 
    (6, "jaga@caltech.edu", 111, False);

INSERT INTO members(user_id, last_name, first_name, preferred_name) VALUES
    (1, "Mo", "Ziyan", "Momo"), 
    (2, "Hu", "Juliette", "Julietto-sama"),
    (3, "Mo", "Ziyan", ""),
    (4, "Wu", "Helena", "Head of Heads"),
    (5, "Shao", "Eugene", "Ugne"),
    (6, "V", "Jagath", "JV");

