from sqlalchemy import create_engine
import csv
import mysql.connector
conn=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
cursor=conn.connect()
data=cursor.execute("SELECT * FROM demo;")
with open(r'test.csv', 'w') as csvfile:
    print(csvfile.name)
    for i in data:
        print(i)
        csv_out = csv.writer(csvfile)
        csv_out.writerow(i)
    

"""with open (r'test.csv','wb') as file:
    reader_variable=csv.reader(file,delimiter =',')
    for row in reader_variable:
        print(row)"""
    



