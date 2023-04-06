class Student:
    __name="Ravi"#private variable
    def __init__(self):
        print(self.__name)#when the object is created then this constructor automatically called
        self.__displayinfo()#we call the private method here
    def __displayinfo(self):
        print("This is a Private Method")

obj=Student()

