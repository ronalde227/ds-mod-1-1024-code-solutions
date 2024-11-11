USE dsstudent;

#QUESTION 1	
 Select TABLE_NAME table_name, TABLE_ROWS row_quantity 
 FROM INFORMATION_SCHEMA.TABLES
 WHERE TABLE_SCHEMA = 'loandb'
 ORDER BY table_name DESC;
 
CREATE TEMPORARY TABLE dsstudent.temp_table(table_name varchar(25),row_quantity BIGINT);

INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "train", count(*) FROM loandb.train;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "bureau", count(*) FROM loandb.bureau;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "bureau_balance", count(*) FROM loandb.bureau_balance;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "previous_application", count(*) FROM loandb.previous_application;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "installments_payments", count(*) FROM loandb.installments_payments;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "POS_CASH_balance", count(*) FROM loandb.POS_CASH_balance ;
INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "credit_card_balance", count(*) FROM loandb.credit_card_balance;


INSERT INTO dsstudent.temp_table(table_name, row_quantity) 
Select "train", count(*) FROM loandb.train
UNION ALL
Select "bureau", count(*) FROM loandb.bureau
UNION ALL
Select "bureau_balance", count(*) FROM loandb.bureau_balance
UNION ALL
Select "previous_application", count(*) FROM loandb.previous_application
UNION ALL
Select "installments_payments", count(*) FROM loandb.installments_payments
UNION ALL
Select "POS_CASH_balance", count(*) FROM loandb.POS_CASH_balance 
UNION ALL
Select "credit_card_balance", count(*) FROM loandb.credit_card_balance;


SELECT * FROM dsstudent.temp_table;

DROP TABLE dsstudent.temp_table;
		
 #QUESTION 2
 SELECT AMT_INCOME_TOTAL annual_income, AMT_INCOME_TOTAL/12 monthly_income FROM loandb.train t 
 
 #Question 3
 SELECT ROUND(DAYS_BIRTH/-365) age
 FROM loandb.train t 
 
  #Question 4
 SELECT OCCUPATION_TYPE occupation_type, Count(*) quantity
 FROM loandb.train t
 WHERE OCCUPATION_TYPE is not NULL 
 GROUP BY OCCUPATION_TYPE
 ORDER BY quantity DESC;
 
#Question 5
SELECT DAYS_EMPLOYED,
CASE 
	WHEN DAYS_EMPLOYED = (SELECT MAX(DAYS_EMPLOYED) FROM loandb.train) THEN "bad data"
	ELSE "normal data"
END "Flag_for_bad_data"
FROM loandb.train t 

#Question 6
SELECT t.target TARGET, min(ip.DAYS_INSTALMENT) min_day_installment, max(ip.DAYS_INSTALMENT) max_day_installment,
min(ip.DAYS_ENTRY_PAYMENT) min_days_entry_payment, max(ip.DAYS_ENTRY_PAYMENT) max_days_entry_payment
FROM loandb.installments_payments ip
	JOIN loandb.credit_card_balance ccb 
	ON ip.SK_ID_PREV = ccb.SK_ID_PREV 
	JOIN loandb.previous_application pa
	ON pa.SK_ID_PREV = ip.SK_ID_PREV 
	JOIN loandb.train t 
	on t.SK_ID_CURR = ip.SK_ID_CURR 
GROUP BY t.target
ORDER BY TARGET;


