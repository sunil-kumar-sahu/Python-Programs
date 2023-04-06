import pandas as pd

dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
d=pd.DataFrame(dis)

d.to_csv("Test_New.csv")
d.to_csv("Test_New1.csv",index=False) #it  will remove the index number
d.to_csv("Test_New2.csv",index=False,header=["col1","col2","col3"]) #it will change the headers of the csv file