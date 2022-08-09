from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
connection=engine.connect()
#print(engine.table_names())
from sqlalchemy import MetaData,Table
metadata=MetaData()
census=Table('t11',metadata,autoload=True,autoload_with=engine)
print(repr(census))

# insert row into table
from sqlalchemy import insert
id=engine.execute("INSERT INTO joget.t11 (id, name, roll_no) VALUES(9, 'Amir', 25)")
print("Row added =",id.rowcount)