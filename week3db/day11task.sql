CREATE DATABASE training_db;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    city VARCHAR(50)
);
INSERT INTO users (name, email, age, city)
VALUES
('Lathi', 'lathi@gmail.com', 22, 'Chennai'),
('sri', 'sri@gmail.com', 25, 'Bangalore'),
('roy', 'roy@gmail.com', 23, 'Hyderabad'),
('emaya', 'emaya@gmail.com', 27, 'Mumbai'),
('Ema', 'ema@gmail.com', 24, 'Delhi');
SELECT * FROM users;
SELECT * FROM users WHERE city = 'Chennai';
SELECT * FROM users WHERE age > 23;
SELECT * FROM users WHERE name LIKE 'L%';
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users ORDER BY age D
SELECT * FROM users ORDER BY name;
SELECT * FROM users WHERE age > 22 ORDER BY name;








