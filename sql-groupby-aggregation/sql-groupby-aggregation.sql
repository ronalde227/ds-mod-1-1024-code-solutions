use telecom;

DROP TABLE dsstudent.temp_table;

CREATE TEMPORARY TABLE dsstudent.temp_table
SELECT t.id, t.location, t.fault_severity, et.event_type,
		st.severity_type, rt.resource_type, lf.log_feature, lf.volume
FROM train t
	LEFT OUTER JOIN severity_type st
	ON t.id = st.id
	LEFT OUTER JOIN resource_type rt
	on rt.id = t.id
	LEFT OUTER JOIN log_feature lf
	on lf.id = t.id
	LEFT OUTER JOIN event_type et
	on et.id = t.id;
#Question 1A
SELECT location, COUNT(DISTINCT(event_type)) "num_unique_event_type"
FROM dsstudent.temp_table
GROUP BY location
ORDER BY location;

#Quesion 1b
SELECT location, sum(volume) "total_volume"
FROM dsstudent.temp_table
GROUP BY location
ORDER BY sum(volume) DESC
LIMIT 3;

#Question 2A
SELECT fault_severity, COUNT(DISTINCT(location)) "num_of_unique_locations"
FROM dsstudent.temp_table
GROUP BY fault_severity;

#Question 2B
SELECT fault_severity, COUNT(DISTINCT(location))
FROM dsstudent.temp_table
GROUP BY fault_severity
HAVING fault_severity > 1;

#Question 3
USE hr;

SELECT * FROM employee;

Select Attrition, MIN(age) min_age, MAX(age) max_age, AVG(age) avg_age
FROM employee
GROUP BY Attrition;

#Question 4

Select Attrition, Department, count(*) "num_quantity"
FROM employee
GROUP BY Attrition, Department
HAVING Attrition IS NOT NULL
ORDER BY Attrition, Department;

#Question 5
Select Attrition, Department, count(*) "num_quantity"
FROM employee
GROUP BY Attrition, Department
HAVING Attrition IS NOT NULL AND num_quantity > 100
ORDER BY Attrition, Department ASC;












