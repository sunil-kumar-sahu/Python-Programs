#Pandas Function
import pandas as pd

csv_1=pd.read_csv("sampledata_sunil1.csv")
#print(csv_1.index) #it will return the total no.of index
#print(csv_1.columns) #it will prints all column name that present in the csv file
#print(csv_1.describe()) #it will show all numerical value column with aggregate value
#print(csv_1.head()) # it will print first 5 row values
#print(csv_1.head(2))#it will print first 2 rows value
#print(csv_1.tail())#it will print last 5 rows value
#print(csv_1[3:9])#it will show the data from 3rd index to 8th index exclude the end index
print(type(csv_1))
#print(csv_1.index.array)#it will show all index number in an array format
#print(csv_1.to_numpy())#it will show the data in numpy format
#print(csv_1.sort_index(axis=0))#it will sort the csv file values in row wise in ascending order
#print(csv_1.sort_index(axis=1,ascending=False))#it will sort the csv file values in col wise in descending order
"""
csv_1["Customer Name"][0]="Sunil"
print(csv_1.to_string())#it will change the Customer Name column first value
"""
#print(csv_1.iloc[0,1])#it will print the 2nd column 1st value
print(csv_1.drop(0,axis=0))#it will drop the 1st row



