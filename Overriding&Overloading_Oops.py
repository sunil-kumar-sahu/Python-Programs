#calculate area of rectangle by using overloading
class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1=Area()
obj1.find_area()
obj1.find_area(5)
obj1.find_area(5,8)
