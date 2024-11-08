USE dsstudent;

#Question 1
CREATE TABLE customer_ronald
	(customer_id smallint,
	 name varchar(20),
	 location varchar(20),
	 total_expenditure varchar(20)
	);
	


#Question 2
INSERT INTO customer_ronald(customer_id, name, location, total_expenditure)
			VALUES(1701, "John", "Newport Beach, CA","2000"),
			(1707, "Tracy", "Irvine, CA","1500"),
			(1711, "Daniel", "Newport Beach, CA","2500"),
			(1703, "Ella", "Santa Ana, CA","1800"),
			(1708, "Mel", "Orange, Ca","1700"),
			(1716, "Steve", "Irvine, CA", "18000");

#Question 3 
UPDATE customer_ronald
SET total_expenditure ="1800"
WHERE customer_id = 1716

#Question 4
ALTER TABLE customer_ronald
ADD gender varchar(20)

#Question 5
UPDATE customer_ronald
SET gender = "F"
UPDATE customer_ronald
SET gender = "M"
WHERE customer_id in (1701, 1711,1716)

#Question 6
DELETE FROM customer_ronald WHERE customer_id = "1716";

#Question 7 
ALTER TABLE customer_ronald
ADD store varchar(20);

#Question 8
ALTER TABLE customer_ronald
DROP COLUMN store;

#Question 9 
SELECT * FROM customer_ronald;

#Question 10
SELECT name, total_expenditure FROM customer_ronald;

#Question 11
SELECT name AS "n", total_expenditure AS "total_exp" FROM customer_ronald;

#Question 12
ALTER TABLE customer_ronald 
MODIFY COLUMN total_expenditure smallint;

#Question 13
SELECT total_expenditure
FROM customer_ronald
ORDER BY total_expenditure desc;

#Question 14
SELECT name, total_expenditure
FROM customer_ronald
ORDER BY total_expenditure DESC
LIMIT 3;

#Question 15
SELECT count(DISTINCT(location)) nuniques
FROM customer_ronald;


#Question 16
SELECT DISTINCT(location) uniques_cities
FROM customer_ronald;




#Question 17
SELECT *
FROM customer_ronald
WHERE gender = 'M';


#Question 18
SELECT *
FROM customer_ronald
WHERE gender = 'F';


#Question 19
SELECT *
FROM customer_ronald
WHERE location = 'Irvine, CA';


#Question 20
SELECT name, location
FROM customer_ronald
WHERE total_expenditure < 2000
ORDER BY name ASC;


#Question 21
DROP TABLE customer_ronald;

SHOW TABLES;

