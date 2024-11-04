
#SELECT/FROM/AS Question 1
SELECT id, log_feature, volume 
FROM log_feature lf ;



#Sorting question 1
SELECT id, resource_type 
FROM resource_type rt 
order by id ASC,resource_type ASC
limit 5;

#Sorting question 2
SELECT id, resource_type 
FROM resource_type rt 
order by id desc,resource_type ASC
limit 5;

#Sorting question 3
SELECT id, resource_type 
FROM resource_type rt 
order by id ASC, resource_type DESC
limit 5;


#Count/distinct
#Question 1
SELECT COUNT(*), COUNT(DISTINCT(id)),count(distinct(severity_type))
FROM severity_type st;

#Where filting 
#Question 1
SELECT id,log_feature,volume 
FROM log_feature lf 
where volume between 100 and 300 AND log_feature ="feature 201"
order by volume ASC;



