import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# df=pd.DataFrame(mydataset)
# print(df)


# # print(pd.__version__)

# #----------Create a simple Pandas Series from a list:----------
# a=[1,7,2]
# df=pd.Series(a)
# print(df)

# #-----Return the first value of the Series:-----
# print(df[0])

# #-----Create your own labels:-----
# a=[1,7,2]
# df=pd.Series(a,index=["x","y","z"])
# print(df)

# #-----Return the value of "y":-----
# print(df["y"])

# #-----Key/Value Objects as Series--Create a simple Pandas Series from a dictionary:----
# calories = {"day1": 420, "day2": 380, "day3": 390}
# df=pd.Series(calories)
# print(df)

# #-----Create a Series using only data from "day1" and "day2":------
# calories = {"day1": 420, "day2": 380, "day3": 390}
# df=pd.Series(calories,index=["day1","day2"])
# print(df)

# # -----------DataFrames---------------

# # Create a DataFrame from two Series:
# data={
#    "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df=pd.DataFrame(data)
# print(df)

# # Locate Row : refer to the row index:
# print(df.loc[0])

# #use a list of indexes:Return row 0 and 1:
# print(df.loc[[0,1]])

# # Named Indexes : Add a list of names to give each row a name:
# data={
#    "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df=pd.DataFrame(data,index=["day1","day2","day3"])
# print(df)

# # Locate Named Indexes : #refer to the named index
# print(df.loc["day2"])


# -------Load Files Into a DataFrame-----------

# Load a comma separated file (CSV file) into a DataFrame:
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df)   #Pandas will only return the first 5 rows, and the last 5 rows

# # Read CSV Files : Load the CSV into a DataFrame
# df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
# print(df.to_string()) #use to_string() to print the entire DataFrame.

# # max_rows
print(pd.options.display.max_rows)   # Check the number of maximum returned rows:

print(df['Amount'].max())  # Check the maximum Amount


#---------Viewing the Data--------
# Head()-----returns the headers and a specified number of rows,starting from the top.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.head(10))
print(df.head())


# tail()-----returns the headers and a specified number of rows, starting from the bottom.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.tail(10))
print(df.tail())

# info()-----that gives you more information about the data set.
# Print information about the data:
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.info())

# Calculating the number of null values
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.isnull().sum())


# =============Most Important Pandas Functions=====================

# read_csv()---reading the dataset.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df)

# head()-----is used to return the first n rows of a dataset,return the first 5 rows of the DataFrame.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.head())
print(df.head(6))

# tail()-----returns the headers and a specified number of rows, starting from the bottom.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.tail(10))
print(df.tail())

# sample()----is used to get a randomly selected row, column, or both from a dataset. 
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.sample())

# info()-----returns a quick summary of the DataFrame.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.info())

# describe()----is used to generate descriptive statistics of the data.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.describe())

# loc[:]---helps to access a group of rows and columns in a dataset.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.loc[0:4, ['City','Date','Card Type']])
print(df.loc[100,'City'])


# unique()---- returns the list of unique values in a column or series
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df['Card Type'].unique())

# isnull()----helps you to check if there in which row and which column your data has missing values.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.isnull())
print(df.isnull().sum())


# sort_values()---helps to arrange the entire DataFrame in ascending or descending order.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.sort_values("Exp Type"))

# value_counts()----returns a Pandas Series containing the counts of unique values.
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df['Card Type'].value_counts())

# # drop_duplicates()----returns a Pandas DataFrame with duplicate rows removed
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.drop_duplicates(inplace=True))   #inplace=True makes sure the changes are applied to the original dataset.

# # memory_usage()---->returns a Pandas Series having the memory usage of each column (in bytes)
df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
print(df.memory_usage(deep=True)) #By specifying the deep attribute as True, we can get to know the actual space being taken by each column.

# astype()----is used to cast a Python object to a particular data type.
# df=pd.read_csv('C:\Career\Excel\Credit_card_transactions.csv')
# df2=df.astype('int64')
# print(df2)





