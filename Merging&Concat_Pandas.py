#Merge
import pandas as pd

var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"A":[1,2,3,5],"C":[21,22,23,24]})
"""
res=pd.merge(var1,var2,on="A")
print(res)#it will merge both dataframe elements into a dictionary by using the common element A
"""
"""
res1=pd.merge(var1,var2,how="inner")
print(res1)#Inner join of two dataframe dictionary
"""
"""
res2=pd.merge(var1,var2,how="left")
print(res2)#Left join of two dictionary
"""
"""
res3=pd.merge(var1,var2,how="outer")
print(res3)#outer join of two dictionary
"""
#Concat
sr1=pd.Series([1,2,3,4])
sr2=pd.Series([11,12,13,14])
"""
res=pd.concat([sr1,sr2])
print(res)#it will concat the series
"""
d1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d2=pd.DataFrame({"A":[1,2],"C":[21,22]})
#print(pd.concat([d1,d2]))#concat the dataframe in row wise
#print(pd.concat([d1,d2],axis=1))#concat the dataframe in column wise

"""
res4=pd.concat([d1,d2],axis=1,join="inner")
print(res4)#it remove the NaN part and merge both dataframe
"""

