CREATE DATABASE exam;
USE exam;
CREATE TABLE Customer
(
    CustomerID int NOT NULL PRIMARY KEY,
    CustomerName varchar(255) NOT NULL,
    City varchar(255) NOT NULL
);

INSERT INTO Customer VALUES (111, 'Abhishek', 'Ahmedabad');
INSERT INTO Customer VALUES (115, 'Aryaman', 'Mumbai');
INSERT INTO Customer VALUES (118, 'Bilal', 'Mumbai');
INSERT INTO Customer VALUES (120, 'Tharun', 'Chennai');
INSERT INTO Customer VALUES (134, 'Rakesh', 'Delhi');