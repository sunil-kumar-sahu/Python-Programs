#join
import pandas as pd
"""
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]},index=["a","b","c","d"])
var2=pd.DataFrame({"C":[10,20],"D":[11,22]},index=["a","b"])
"""
"""
c=var1.join(var2)#it is used to join two dataframe
print(c)
"""
#print(var2.join(var1,how="right"))#it will perform right join
#print(var2.join(var1,how="inner"))#it will perform intersection of both data
#print(var2.join(var1,how="outer"))#it will perform union of both data frames
"""
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]},index=["a","b","c","d"])
var2=pd.DataFrame({"C":[10,20],"B":[11,22]},index=["a","b"])
print(var2.join(var1,how="outer",lsuffix="_12",rsuffix="_123"))#it will change the column name of B
"""

#Append
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"C":[10,20],"B":[11,22]})
print(var1.append(var2,ignore_index=True))