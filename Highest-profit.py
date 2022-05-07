#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install Pandas
get_ipython().system('pip install pandas')


# In[2]:


# Importing Pandas Module
import pandas as pd 

# Reading CSV file and Printing Number of Rows in the data.
csv_file = pd.read_csv('data.csv')
print ("Number of rows in the data:", len(csv_file))
csv_file


# In[3]:


# Identify and show the null value/non-numeric value rows in the data
null_rows = (csv_file[pd.to_numeric(csv_file['Profit (in millions)'], errors='coerce').isnull()])
null_rows.head(10)
null_rows


# In[4]:


# identifying and seperating Numeric i.e. correct data from the original data.
data_columns = ['Profit (in millions)']

# Dropping the column first and passing the column through pd.to_numeric to convert all non-numeric entries to NaN
drop_data = (csv_file.drop(data_columns, axis=1).join(csv_file[data_columns].apply(pd.to_numeric, errors='coerce')))

# Adding the column back in the data correctly.
cleaned_data = drop_data[drop_data[data_columns].notnull().all(axis=1)]

#Dropping rows with NA value in 'Profit' columns
cleaned_data.dropna(subset = ['Profit (in millions)'])
cleaned_data


# In[5]:


# Storing the output of the Cleaned Data in 'data2.json'
cleaned_data.to_json(path_or_buf='data2.json',orient='records',lines=True)


# In[6]:


# Sorting Data and columns based on 'Profit(in Millions)' in Descending order
sorted_data = cleaned_data.sort_values(by='Profit (in millions)',ascending=False)

sorted_data.head(20)           # Printing top 20 Profit values


# In[7]:


# Storing Sorted data by profit in 'data_sorted.json'
sorted_data.to_json(path_or_buf='data_sorted.json',orient='records',lines=True)

