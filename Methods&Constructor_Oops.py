class DemoClass:
    a=10
    def __init__(self):#Constructor
        print("Well Come To Sunny World")

    def showvalues(self):#function with no argument and by using self we use the member variable
        self.c=self.a*self.a
        print(self.c)

    def showvalues1(self,a,b):#function with argumets
        print(a+b)

obj=DemoClass()
obj.showvalues()
obj.showvalues1(28,56)