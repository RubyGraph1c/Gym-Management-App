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


INSERT INTO members(name, id) VALUES ('Lucinda Shale', 1111);
INSERT INTO members(name, id) VALUES ('Evelyn Clementine', 2222);
INSERT INTO members(name, id) VALUES ('Katie Buchan', 3333); 
INSERT INTO members(name, id) VALUES ('Dominique Haig', 4444); 
INSERT INTO members(name, id) VALUES ('Rowan Wood', 5555);
INSERT INTO members(name, id) VALUES ('Charlie Shale', 6666); 
INSERT INTO members(name, id) VALUES ('Emily Swed', 7777); 
INSERT INTO members(name, id) VALUES ('Jennifer Jane', 8888); 

-- SESSIONS: MONDAY

INSERT INTO sessions (name, day, time, id) VALUES ('Vinyasa Yoga', 'Monday', '9AM', 10); 

INSERT INTO sessions (name, day, time, id) VALUES ('Body Pump', 'Monday', '4PM', 11); 

-- SESSIONS: TUESDAY 


INSERT INTO sessions (name, day, time, id) VALUES ('Body Balance', 'Tuesday', '9AM', 12); 

INSERT INTO sessions (name, day, time, id) VALUES ('Body Combat', 'Tuesday', '4PM', 13); 

-- -- SESSIONS: WEDNESDAY 

INSERT INTO sessions (name, day, time, id) VALUES ('YoPi', 'Wednesday', '9AM', 14); 

INSERT INTO sessions (name, day, time, id) VALUES ('Body Attack', 'Wednesday', '4PM', 15); 

-- -- SESSIONS: THURSDAY

INSERT INTO sessions (name, day, time, id) VALUES ('Stretch', 'Thursday', '9AM', 16); 

INSERT INTO sessions (name, day, time, id) VALUES ('Zumba', 'Thursday', '4PM', 17); 

-- -- SESSIONS: FRIDAY 

INSERT INTO sessions (name, day, time, id) VALUES ('Pilates', 'Friday', '9AM', 18); 

INSERT INTO sessions (name, day, time, id) VALUES ('HIIT', 'Friday', '4PM', 19); 

-- -- SESSIONS: SATURDAY 

INSERT INTO sessions (name, day, time, id) VALUES ('Tai Chi', 'Saturday', '9AM', 20); 

INSERT INTO sessions (name, day, time, id) VALUES ('Aerobics', 'Saturday', '4PM', 21); 

-- -- SESSIONS: SUNDAY 

INSERT INTO sessions (name, day, time, id) VALUES ('Crossfit', 'Sunday', '9AM', 22); 

INSERT INTO sessions (name, day, time, id) VALUES ('LB&T', 'Sunday', '4PM', 23); 

 
