import pandas as pd
"""
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
#print(var)

#var["C"]=var["A"]+var["B"]
#var["C"]=var["A"]*var["B"]
#var["C"]=var["A"]-var["B"]
var["C"]=var["A"]/var["B"]
print(var)
"""
var1=pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})
var1["Python"]=var1["A"] <= 20 #it will check whether the value of A element is <= 20,if it is satisfies then it will print true in Python column
var1["Python_1"]=var1["B"] >= 16
print(var1)



