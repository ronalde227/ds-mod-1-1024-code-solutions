# -*- coding: utf-8 -*-
"""Pandas_Exercises.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RnKf8MtIYKPl7jsaAjiTdxfdUhxVnkGc

# Pandas Exercises

### 1. Import numpy, pandas, etc
"""

import numpy as np

import pandas as pd
# import ....

"""### 2. Load the data from the file `"Loan payments data.csv"` into a variable called `"loans"`"""

loans = pd.read_csv("/content/Loan payments data.csv")
loans

"""### 3. Display the first 7 rows of the data"""

loans.head(7)

"""### 4. Display the last 3 rows of the data"""

loans.tail(3)

"""### 5. Select 25% of the data, picked randomly and display the first 5 rows"""

loans.sample(frac=0.25).head(5)

"""### 6. Sample 10 rows and display it"""

loans.sample(10)

"""### 7. Display the value counts of the `loan_status` column and the `City` column"""

loans['loan_status'].value_counts()

loans.City.value_counts()

"""### 8. Display only the 201st row"""

loans.iloc[200]

"""### 9. Display only the `education` column"""

oans['education']

"""### 10. Display only the `loan_status` column"""

loans['loan_status']

"""### 11. Display only the 9th column by index

***(hint: remember that Python is 0-indexed!)***
"""

loans.iloc[:, 8]

"""### 12. Display the 3rd through 7th rows by index slicing"""

loans.iloc[3:8]

"""### 13. Display the last 3 columns by index slicing"""

loans.iloc[:,-3:]

"""### 14. Display only the rows where `Gender` is `female`"""

loans[loans["Gender"]=="female"]

"""### 15. Display only the rows where `education` is `college` AND `City` is `NYC`"""

loans[(loans["education"]=="college")&(loans["City"]=="NYC")]

"""### 16. Display only the rows where `age` is larger than 32"""

loans[loans.age > 32]

"""### 17.  Display the rows where there is a past-due of larger than a week and only display the `due_date` and `past_due_days` columns"""

loans[loans.past_due_days > 7][['due_date', 'past_due_days']]