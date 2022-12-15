CREATE DATABASE exam;
USE exam;
CREATE TABLE Book
(
    Code char(4) NOT NULL,
    Bname varchar(255) NOT NULL,
    Type varchar(30) NOT NULL
);

INSERT INTO Book VALUES('F101', 'The Priest', 'Fiction');
INSERT INTO Book VALUES('L102', 'German Easy', 'Literature');
INSERT INTO Book VALUES('F101', 'Untold Story', 'Fiction');
INSERT INTO Book VALUES('C101', 'Tarzan in the Lost World', 'Comic');
INSERT INTO Book VALUES('C102', 'War Heroes', 'Comic');