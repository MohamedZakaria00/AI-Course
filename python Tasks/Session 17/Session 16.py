#!/usr/bin/env python
# coding: utf-8

# **Task 1: Read Text from Database**        

# In[1]:


import pyodbc
import pandas as pd

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\hp\Untitled Folder 1\Database1.accdb;')

SQL_Query = pd.read_sql_query('''select 
name,
age
from test''',conn)
df = pd.DataFrame(SQL_Query, columns=['name','age'])
df


# **Task 2: How to change comlumn in pandas**

# In[2]:


import pandas as pd
df = pd.read_excel("Test.xlsx")
df


# In[3]:


df = df.rename(columns={'event':'The State'})
df


# In[ ]:




