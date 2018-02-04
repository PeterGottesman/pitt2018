DROP TABLE reviews, reviewers;

CREATE TABLE reviewers
(
reviewerID SERIAL PRIMARY KEY,
lastName VARCHAR (255),
firstName VARCHAR (255),
specialty VARCHAR (255),
experience INT,
authentication TINYINT (1)
);

CREATE TABLE reviews
(
ratingID SERIAL NOT NULL PRIMARY KEY,
url VARCHAR (2083),
title VARCHAR (255),
author VARCHAR (255),
rating TINYINT,
reviewerID BIGINT UNSIGNED NOT NULL,
FOREIGN KEY (reviewerID) REFERENCES reviewers(reviewerID)
);


INSERT INTO reviewers VALUES (1337, "Phil", "Dr", "Bullshit", 100, 1);
INSERT INTO reviewers VALUES (420, "Oz", "Dr", "Bullshit", 24, 0);
INSERT INTO reviewers VALUES (666, "Strangelove", "Dr", "Weaponry", 67, 1);
INSERT INTO reviewers VALUES (1234, "Jekyll", "Dr", "Bullshit", 13, 1);
