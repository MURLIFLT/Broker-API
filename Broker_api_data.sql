CREATE DATABASE broker_db;
USE broker_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(50) UNIQUE NOT NULL,
    price FLOAT NOT NULL
);
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    symbol VARCHAR(50) NOT NULL,
    order_type VARCHAR(10) NOT NULL CHECK (order_type IN ('BUY', 'SELL')),
    quantity INT NOT NULL,
    price FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
SHOW TABLES;
SELECT * FROM users;
INSERT INTO users (username, password) VALUES ('john_doe', 'securepassword');
SELECT id FROM users WHERE username = 'john_doe';
INSERT INTO orders (user_id, symbol, order_type, quantity, price) 
VALUES (1, 'AAPL', 'BUY', 10, 150.50);
INSERT INTO users (username, password) VALUES ('john_doe', 'securepassword');

INSERT INTO market_data (symbol, price) VALUES ('AAPL', 150.75), ('TSLA', 800.50);


SELECT * FROM users;
SELECT * FROM market_data;
SELECT * FROM orders;
