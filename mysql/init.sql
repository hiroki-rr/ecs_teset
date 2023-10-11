CREATE DATABASE testdb;

USE testdb;

CREATE TABLE test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_column VARCHAR(255) NOT NULL
);

INSERT INTO test (test_column) VALUES ("test");

