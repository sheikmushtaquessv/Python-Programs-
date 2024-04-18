import pandas as pd

csv_file = 'pandas_class_sample.csv'

sample_dict = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

# To read a dictionar into a dataframe
df = pd.DataFrame(sample_dict)
# To read a csv file into a dataframe
df2 = pd.read_csv(csv_file)
# to print first 5 rows
# print(df2.head())

# to print dataframe information
# print(df2.info())

# to print descriptive statistics of numeric columns
# print(df2.describe())

# to print column names
# print(df2.columns)

# to print specific columns
# columns_required = ['First_Name','Email']
# print(df2[columns_required])

# to print filtered dataframe
condition = df2['City'].str.contains('bad')
condition2 = df2['S.No'] > 3
print(df2[condition2])



