
CREATE DATABASE IF NOT EXISTS StudentAnalysis;

USE StudentAnalysis;

CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    marks INT,
    age INT
);
