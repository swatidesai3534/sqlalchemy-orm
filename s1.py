import csv
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import insert
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
connection=engine.connect()
#sql='select * from demo'
data=connection.execute(text("select *from demo"))
print(data.all())

