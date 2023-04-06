import pandas as pd
"""
data = pd.read_csv('sampledata_sunil1.csv')
print(data.to_string())#it is used to return the entire dataframe
"""
#print(pd.options.display.max_rows) #it will display the maximum number of rows

#Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows=9999
df=pd.read_csv('sampledata_sunil1.csv')
print(df)
