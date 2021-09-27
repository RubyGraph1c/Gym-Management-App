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
    category VARCHAR(255),
    day VARCHAR (255),
    time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members (id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions (id) ON DELETE CASCADE,
    confirmation BOOLEAN
    );

-- INSERT INTO members (name) VALUES (member.name);
-- INSERT INTO members (name) VALUES ('Murray Grant');
-- INSERT INTO members (name) VALUES ('Dominique Haig');
-- INSERT INTO members (name) VALUES ('Rowan Wood');

-- INSERT INTO sessions (name, category, day, time) 
-- VALUES ({session.name}, {session.category}, {session.day}, {session.time});

-- INSERT INTO sessions (name, category, day, time) 
-- VALUES ('Body Balance', 'Yoga/Pilates', "Wednesday", "10.00AM");

-- INSERT INTO sessions (name, category, day, time) 
-- VALUES ('Body Attack', 'HIIT', "Friday", "11.00AM");

-- INSERT INTO sessions (name, category, day, time) 
-- VALUES ('Body Combat', 'Aerobic', "Sunday", "12.00PM");

-- INSERT INTO bookings (session_id, member_id, confirmation) VALUES (True);
-- INSERT INTO bookings (session_id, member_id, confirmation) VALUES (False);
-- INSERT INTO bookings (session_id, member_id, confirmation) VALUES (True);
-- INSERT INTO bookings (session_id, member_id, confirmation) VALUES (False);

