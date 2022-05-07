# Shriniwas_SADA_assesment
This repository contains a solution to one of the challenges provided for the SADA assessment.
(Please find below the changes made form the last submission)
# Highest-Profit
This solution is for the Highest-Profit challenge mentioned. 

The following is the description of the files in the repository:

**1. Highest-profit.ipynb** - Jupiter notebook executable code with examples

**2. data.csv** - Original Raw data file

**3. data2.json** - Cleaned data file with only numeric values for the “Profit(in millions)” column.

**4. data_sorted.json** - This file contains the cleaned sorted data required for the challenge.

# WorkFlow with examples
1. First we install pandas.

2. Using pandas to read the data file.

3. Check the number of rows in the data.

![image](https://user-images.githubusercontent.com/82992833/166964501-f280748e-1449-4d8b-8ba8-94a57578be12.png)

4. Checked data for non-numeric values in the Profit column.

![image](https://user-images.githubusercontent.com/82992833/166965128-24b01e16-cfc9-4ccf-982f-90f3a41af3f9.png)

5. Removed the rows containing non-numeric values in the Profit column.

6. Check the number of rows in the cleaned data.

![image](https://user-images.githubusercontent.com/82992833/166965099-583a4a7a-2b21-4eb7-b893-cfeb8d68da10.png)

5. Stored the required output in “data2.json” file.

![image](https://user-images.githubusercontent.com/82992833/166964884-144211e4-76bd-4163-a6a4-ff026286a4a6.png)

6. Sorted the data by the “Profit” column in Descending order.

7. Printed top 20 records of the data.

![image](https://user-images.githubusercontent.com/82992833/167268025-3dc7df81-8d53-48ef-ac44-f8d95598b9ff.png)

8. Additionally, sorted the sorted and cleaned data output in “data_sorted.json” file.

![image](https://user-images.githubusercontent.com/82992833/167268038-02da07ff-5890-4d52-b537-bae7cf097fad.png)

# Changes:
The 'Profit' column after extracting was a data type of object and had to be converted to float to get the correct sorted output.
The code describes the changes mendtioned with description.

# Additional-note
We could solve this challenge using SQL as well. But as the data was small and could fit into the memory using pandas in python and using SQL has no performance difference. If the data would be large, using SQL primarily in BigQuery would be faster and easier.
Below is the SQL code used in BigQuery
