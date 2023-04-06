import pandas as pd

var=pd.DataFrame({"name":["a","b","c","d","a","b","a","b","a","c","c","d"],
                  "S_1":[12,13,14,12,13,14,15,23,25,16,10,34],
                "S_2":[23,24,25,26,27,28,29,30,25,34,35,56]})

var_new=var.groupby("name")

"""
for x,y in var_new:
    print(x)
    print(y)
    print()
    """

#print(var_new.get_group("a"))#it will group the 'a' columns value

#print(var_new.min())#to get the min data of all column of both s1 and s2
#print((var_new.max()))#to get maximum data of all column of both s1 and s2
print(var_new.mean())#to calculate the mean of all column