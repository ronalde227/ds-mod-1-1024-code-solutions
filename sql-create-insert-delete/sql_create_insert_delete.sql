USE dsstudent;

CREATE TABLE person_ronald
		(person_id INT,
		first_name varchar(25),
		last_name varchar(25),
		city varchar(25),
		CONSTRAINT pk_person_ronald PRIMARY KEY (person_id));

SELECT * FROM person_ronald;
		

INSERT INTO person_ronald(person_id, first_name,last_name, city)
	VALUES(1, "Ronald", "Melendez", "Whittier");

INSERT INTO person_ronald(person_id, first_name,last_name, city)
	VALUES(2, "Jennifer", "Oliva", "Los Angeles"),
		  (3, "Carlos", "Pena", "Irvine");

#adding column
Alter Table person_ronald
ADD gender varchar(20);


UPDATE person_ronald
SET gender = "Male"
where person_id in (1,3);

UPDATE person_ronald
SET gender = "Female"
where person_id = 2;


#Delete column
ALTER TABLE person_ronald
DROP COLUMN gender;

DELETE FROM person_ronald
where person_id = 2;

#DELETE TABLE
DROP TABLE person_ronald;

SHOW TABLES;
