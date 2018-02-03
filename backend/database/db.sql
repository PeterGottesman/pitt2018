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
ratingID SERIAL,
url VARCHAR (2083),
title VARCHAR (255),
author VARCHAR (255),
rating TINYINT,
reviews BIGINT
);