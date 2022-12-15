CREATE DATABASE exam;
USE exam;
CREATE TABLE Medicine
(
    DrugId int PRIMARY KEY NOT NULL,
    DrugName varchar(255) NOT NULL,
    Price float NOT NULL
);

INSERT INTO Medicine VALUES(5476, 'Amlodipin', 100.00);
INSERT INTO Medicine VALUES(2345, 'Paracetamol', 10.75);
INSERT INTO Medicine VALUES(1236, 'Nebistar', 60.50);
INSERT INTO Medicine VALUES(6512, 'Vitaplus', 150.50);
INSERT INTO Medicine VALUES(5631, 'Covishield', 1050.50);