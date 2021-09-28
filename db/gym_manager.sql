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

-- check tables 

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members (id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions (id) ON DELETE CASCADE
    );


INSERT INTO members(name, id)
VALUES ('Lucinda Shale', 2222);

INSERT INTO members(name, id)
VALUES ('Charlie Shale', 3333)

-- create form/create member (similar form for edit)

-- MONDAY

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Monday', '9.00 AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Balance', 'YoPi', 'Monday', '5.00 PM');

-- TUESDAY

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Tuesday', '8.00 AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Tuesday', '4.00 PM');

-- WEDNESDAY

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Wednesday', '7.00 AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Wednesday', '3.00 PM');

-- THURSDAY

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Thursday', '10.00 AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Thursday', '6.00 PM');

-- FRIDAY 

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Friday', '9.00AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Friday', '9.00AM');

-- SATURDAY

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Saturday', '11.00 AM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Saturday', '7.00 PM');

-- SUNDAY 

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Sunday', '12.00 PM');

INSERT INTO sessions(name, category, day, time, id)
VALUES ('Body Pump', 'Weight-lifting', 'Sunday', '8.00 PM');



