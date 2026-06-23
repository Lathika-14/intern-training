CREATE DATABASE sqladvance;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR UNIQUE,
    city VARCHAR(50)
);
INSERT INTO users (name, email, city) VALUES
('Shyam', 'shyam@gmail.com', 'Chennai'),
('Ram', 'ram@gmail.com', 'Bangalore'),
('Hari', 'hari@gmail.com', 'Hyderabad'),
('Priya', 'priya@gmail.com', 'Chennai'),
('Anu', 'anu@gmail.com', 'Mumbai');
SELECT * FROM users;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO posts (title, content, user_id) VALUES
('SQL Basics', 'Learning SQL', 1),
('PostgreSQL', 'Working with PostgreSQL', 1),
('FastAPI CRUD', 'Building APIs', 2),
('Python Tips', 'Useful tricks', 3),
('Database Design', 'Normalization', 2),
('REST API', 'Understanding REST', 1);
SELECT * FROM posts ; 
UPDATE posts SET title = 'Advanced PostgreSQL' WHERE id = 2;
SELECT * FROM posts; 
DELETE FROM posts WHERE id = 5;
SELECT * FROM posts; 
SELECT posts.id,posts.title,users.name FROM posts INNER JOIN users ON posts.user_id = users.id;
SELECT users.id,users.name,posts.title FROM users LEFT JOIN posts ON users.id = posts.user_id;
SELECT COUNT(*) AS total_posts FROM posts;
SELECT users.name, COUNT(posts.id) AS total_posts FROM users
LEFT JOIN posts
ON users.id = posts.user_id
GROUP BY users.name;

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product VARCHAR(50),
    amount INT
);
INSERT INTO sales (product, amount)
VALUES
('Laptop', 50000),
('Mouse', 1000),
('Keyboard', 2000),
('Monitor', 15000);
SELECT * FROM sales;
SELECT SUM(amount) AS total_sales FROM sales;
SELECT AVG(amount) AS average_sales FROM sales;
CREATE INDEX idx_sales ON sales(product);
SELECT * FROM sales WHERE product = 'Laptop';