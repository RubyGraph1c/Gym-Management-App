DROP TABLE bookings;
DROP TABLE members; 
DROP TABLE sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    day VARCHAR (255),
    time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members (id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions (id) ON DELETE CASCADE 
    );


-- MEMBERS:

INSERT INTO members(name) VALUES ('Lucinda Shale');
INSERT INTO members(name) VALUES ('Evelyn Clementine');
INSERT INTO members(name) VALUES ('Katie Buchan'); 
INSERT INTO members(name) VALUES ('Dominique Haig'); 
INSERT INTO members(name) VALUES ('Rowan Wood');
INSERT INTO members(name) VALUES ('Charlie Shale'); 
INSERT INTO members(name) VALUES ('Emily Swed'); 
INSERT INTO members(name) VALUES ('Jennifer Jane'); 

-- SESSIONS:

INSERT INTO sessions (name, day, time) VALUES ('Vinyasa Yoga', 'Monday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('Body Pump', 'Monday', '4PM'); 


INSERT INTO sessions (name, day, time) VALUES ('Body Balance', 'Tuesday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('Body Combat', 'Tuesday', '4PM'); 


INSERT INTO sessions (name, day, time) VALUES ('Beginners Yoga', 'Wednesday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('Body Attack', 'Wednesday', '4PM'); 


INSERT INTO sessions (name, day, time) VALUES ('Stretch Class', 'Thursday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('Zumba (Dance)', 'Thursday', '4PM'); 


INSERT INTO sessions (name, day, time) VALUES ('Pilates Int', 'Friday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('HIIT Training', 'Friday', '4PM'); 


INSERT INTO sessions (name, day, time) VALUES ('Tai Chi (60+)', 'Saturday', '9AM'); 
INSERT INTO sessions (name, day, time) VALUES ('Aerobics', 'Saturday', '4PM'); 


-- NO DEFAULT CLASSES ON A SUNDAY


--BOOKINGS:

INSERT INTO bookings(member_id, session_id) VALUES (1, 1);
INSERT INTO bookings(member_id, session_id) VALUES (1, 2);
INSERT INTO bookings(member_id, session_id) VALUES (1, 3);
INSERT INTO bookings(member_id, session_id) VALUES (2, 4);
INSERT INTO bookings(member_id, session_id) VALUES (2, 5);
INSERT INTO bookings(member_id, session_id) VALUES (2, 6);

INSERT INTO bookings(member_id, session_id) VALUES (3, 7);
INSERT INTO bookings(member_id, session_id) VALUES (3, 8);
INSERT INTO bookings(member_id, session_id) VALUES (3, 9);
INSERT INTO bookings(member_id, session_id) VALUES (4, 10);
INSERT INTO bookings(member_id, session_id) VALUES (4, 11);
INSERT INTO bookings(member_id, session_id) VALUES (4, 12);

INSERT INTO bookings(member_id, session_id) VALUES (5, 1);
INSERT INTO bookings(member_id, session_id) VALUES (5, 2);
INSERT INTO bookings(member_id, session_id) VALUES (5, 3);
INSERT INTO bookings(member_id, session_id) VALUES (6, 4);
INSERT INTO bookings(member_id, session_id) VALUES (6, 5);
INSERT INTO bookings(member_id, session_id) VALUES (6, 6);

INSERT INTO bookings(member_id, session_id) VALUES (7, 7);
INSERT INTO bookings(member_id, session_id) VALUES (7, 8);
INSERT INTO bookings(member_id, session_id) VALUES (7, 9);
INSERT INTO bookings(member_id, session_id) VALUES (8, 10);
INSERT INTO bookings(member_id, session_id) VALUES (8, 11);
INSERT INTO bookings(member_id, session_id) VALUES (8, 12);
