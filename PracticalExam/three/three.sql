CREATE DATABASE exam;
USE exam;
CREATE TABLE student
(
    StuID char(5) PRIMARY KEY NOT NULL,
    Name varchar(255) NOT NULL,
    Class char(3) NOT NULL
);

INSERT INTO student VALUES ('12A07', 'Tanmay', '12A');
INSERT INTO student VALUES ('11B10', 'Shreya', '11B');
INSERT INTO student VALUES ('12B18', 'Kavya', '12B');
INSERT INTO student VALUES ('11C10', 'Akshay', '11C');