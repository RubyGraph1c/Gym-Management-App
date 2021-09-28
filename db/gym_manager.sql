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

-- SESSIONS: MONDAY

INSERT INTO sessions (name, day, time) VALUES ('Vinyasa Yoga', 'Monday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('Body Pump', 'Monday', '4PM'); 

-- SESSIONS: TUESDAY 


INSERT INTO sessions (name, day, time) VALUES ('Body Balance', 'Tuesday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('Body Combat', 'Tuesday', '4PM'); 

-- -- SESSIONS: WEDNESDAY 

INSERT INTO sessions (name, day, time) VALUES ('YoPi', 'Wednesday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('Body Attack', 'Wednesday', '4PM'); 

-- -- SESSIONS: THURSDAY

INSERT INTO sessions (name, day, time) VALUES ('Stretch', 'Thursday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('Zumba', 'Thursday', '4PM'); 

-- -- SESSIONS: FRIDAY 

INSERT INTO sessions (name, day, time) VALUES ('Pilates', 'Friday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('HIIT', 'Friday', '4PM'); 

-- -- SESSIONS: SATURDAY 

INSERT INTO sessions (name, day, time) VALUES ('Tai Chi', 'Saturday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('Aerobics', 'Saturday', '4PM'); 

-- -- SESSIONS: SUNDAY 

INSERT INTO sessions (name, day, time) VALUES ('CrossFit', 'Sunday', '9AM'); 

INSERT INTO sessions (name, day, time) VALUES ('LB&T', 'Sunday', '4PM');

--BOOKINGS:

INSERT INTO bookings(member_id, session_id) VALUES (1, 2);