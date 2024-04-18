import pandas as pd

# csv_file ='C:\Career\Excel\weather_data.csv'
csv_file ='C:\Career\Excel\pandas_class_sample.csv'


sample_dict = {
        'id':[101,202,345],
        'Age': [25.63, 30.12, 35.12],
        'name':['John','cena','rohit']  
        
}
# # To read a dictionar into a dataframe
# df = pd.DataFrame(sample_dict)

# # To read a csv file into a dataframe
# # df2=pd.read_csv('C:\Career\Excel\weather_data.csv')
df2=pd.read_csv(csv_file)
print(df2)

# # to print first 5 rows
# print(df2.head())

# # to print dataframe information
# print(df2.info())

# # to print descriptive statistics of numeric columns
# print(df2.describe())

# # to print column names
# print(df2.columns)

# # astype()
# df=pd.DataFrame(sample_dict)
# df2=df.astype('object')
# print(df2)


# to print specific columns
#  df2[['Email','Phone']] 
# columns_required=['First Name','Email']
# print(df2[columns_required])

# # to print filtered dataframe
# condition=df2['City'].str.contains('bad')
# condition2=df2['S.NO'] > 3
# Print(df2[condition2])