CREATE DATABASE exam;
USE exam;
CREATE TABLE Stationery
(
    SID char(4) PRIMARY KEY NOT NULL,
    StationeryName varchar(50) NOT NULL,
    Price float NOT NULL
);

INSERT INTO Stationery VALUES('DP01', 'Dot Pen', 10);
INSERT INTO Stationery VALUES('PL02', 'Pencil', 6);
INSERT INTO Stationery VALUES('ER05', 'Eraser', 7);
INSERT INTO Stationery VALUES('GP02', 'Gel Pen', 15);