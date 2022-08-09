"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is  " + self.name)
p1=Person("John",36)
p1.myfunc() """



"""class Person():
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def myfunc(abc):
        print("Hello my name is  "+abc.name)
p1=Person("John",36)
p1.myfunc()"""


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print("Hello my name is " +self.firstname)
p1=Person("John","Deo")
p1.printname() 

class Student(Person):
    pass

p1=Student("John","Deo")
p1.printname()


