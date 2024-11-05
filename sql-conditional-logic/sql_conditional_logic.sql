#Question 1
#Part 1
Select * 
FROM log_feature lf ;

SELECT id, log_feature, volume,
	case
		WHEN volume < 100 THEN "low"
		WHEN volume > 500 THEN "high_wage"
		ELSE "medium"
	end AS "Volume 1"
FROM log_feature lf;

DROP dsstudent.volume_table;

#Part 2
CREATE TEMPORARY TABLE dsstudent.volume_table
SELECT id, log_feature, volume,
	case
		WHEN volume < 100 THEN "low"
		WHEN volume > 500 THEN "high_wage"
		ELSE "medium"
	end AS "Volume 1"
FROM log_feature lf;

SELECT `Volume 1`,COUNT(`Volume 1`) 
FROM dsstudent.volume_table
GROUP BY `Volume 1`;

#Question 2

USE hr;

SELECT EmployeeNumber, HourlyRate, 
	case
		WHEN HourlyRate < 40 THEN "low hourly rate"
		WHEN HourlyRate >= 80 THEN "high hourly rate"
		ELSE "midium hourly rate"
	end AS "HourlyRate_1"
FROM employee;

#Question 3

SELECT Gender,
CASE
	WHEN Gender = "Female" THEN 0
	WHEN Gender = "Male" THEN 1
END AS "Gender_1"
FROM employee;









