# -*- coding: utf-8 -*-
"""thanksgiving.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1exWw_2EYNKhSQF-MnosyhulB16oB4d7g

#Thanksgiving
"""

import datetime as dt

today = dt.date.today()
today

thanksgiving_date = dt.date(2024,11,28)

deltaTime = thanksgiving_date - today

print("Days till thanksgiving: "+str(deltaTime))