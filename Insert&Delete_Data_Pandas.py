import pandas as pd
#Insert Data into the DataFrame
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5],"C":[12,13,14,15,16]})
"""
var.insert(1,"python",var["A"]) #insert a column name python in 2nd postion having values of same A elements
print(var)
"""
"""
var["Python_12"]=var["A"][:3]
print(var)
"""

#Delete Data into DataFrame
var1=var.pop("B") # it will delete the B's Data
print(var1)

del var["A"] #it will delete the A's Data
print(var)
