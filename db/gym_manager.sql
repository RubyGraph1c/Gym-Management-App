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
    day VARCHAR (255)
    members VARCHAR(255)
);

-- Day and time instead of date? Session won't have members - booking will? 


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members (id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions (id) ON DELETE CASCADE,
    CONFIRMATION TEXT
);

-- date_and_time DATETIME?

