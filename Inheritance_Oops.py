class A:
    def displayA(self):
        print("WellCome to SunnyWorld A")

class B(A):#Class B Inherits Class A(single inheritance)
    def displayB(self):
        print("WellCome to SunnyWorld B")

class C(B):#Multiple inheritance
    def displayC(self):
        print("Multiple Inheritance C")

"""
class C(A,B):#Multiple inheritance
    def displayC(self):
        print("Multilevel Inheritance C")
        """

obj=C()
obj.displayA()#By using C's Object we call A's Method
obj.displayB()
obj.displayC()
