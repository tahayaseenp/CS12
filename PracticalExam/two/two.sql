CREATE DATABASE `exam`;
USE `exam`;
CREATE TABLE Employee
(
    Empno int PRIMARY KEY NOT NULL,
    Empname varchar(255) NOT NULL,
    Age int NOT NULL
);

INSERT INTO Employee VALUES (1, 'Ankit', 45);
INSERT INTO Employee VALUES (2, 'Sumit', 32);
INSERT INTO Employee VALUES (3, 'Suchitra', 23);
INSERT INTO Employee VALUES (4, 'Amit', 25);
INSERT INTO Employee VALUES (5, 'Ankita', 26);