from codecs import getencoder
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
connection=engine.connect()
class Demo:
    def __init__(self,id,first_name,last_name):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
    def printname(self):
        print("My name first name is  "+self.first_name)
        print("my name last name is "+ self.last_name)
p1=Demo(3,"john","Deo")
p1.printname()