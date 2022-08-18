from ast import Delete
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table,Integer,String,MetaData,ForeignKey,Column,Numeric
# creating table
engine = create_engine("mysql+pymysql://root:root@localhost:3306/joget")
metadata=MetaData(bind=engine)
MetaData.reflect(metadata)
books=Table('book',metadata,Column('book_id',Integer,primary_key=True),
                            Column('book_price',Numeric),
                            Column('genre',String(30)),
                            Column('book_name',String(30)),extend_existing=True)
metadata.create_all(engine)
# insert record into the table
statement1=books.insert().values(book_id=1,book_price=12.2,genre='fiction',book_name='Old age')
statement2=books.insert().values(book_id=2,book_price=13.2,genre='non-fiction',book_name='Saturn rings')
statement3=books.insert().values(book_id=3,book_price=121.6,genre='fiction',book_name='Supernova')
statement4=books.insert().values(book_id=4,book_price=100,genre='non-fiction',book_name='History of the world')
statement5=books.insert().values(book_id=5,book_price=1112.2,genre='fiction',book_name='sun city')
# execute the insert record into statement
engine.execute(statement1)
engine.execute(statement2)
engine.execute(statement3)
engine.execute(statement4)
engine.execute(statement5)

from sqlalchemy import text
sql=text('select * from book where book.book_price>50')
result=engine.execute(sql)

# view the records
for record in result:
    print("\n",record)



"""inspector=inspect(engine)
inspector.get_columns('book')
print(inspector.get_columns('book'))"""

# Inserting a record using raw SQL Query in SQLAlchemy
data =( { "book_id":6, "book_price":400, "genre":"fiction","book_name":"yoga is science"},
        {"book_id":7,"book_price":800,"genre":"non-fiction","book_name":"alchemy tutorial"},)
statement=text('INSERT INTO book (book_id,book_price,genre,book_name) values(:book_id,:book_price,:genre,:book_name)')
for line in data:
    engine.execute(statement,**line)

sql=text('select*from book')
result=engine.execute(sql)

for record in result:
    print(record)

## to fetch record in sqlalchemy
query=sqlalchemy.select(books).where(books.c.genre=='fiction')
result=engine.execute(query)

## fetch all the records
result=engine.execute(query).fetchall()

# view the records
for record in result:
    print("\n",record)

#SQLAlchemy Query to use sum and order by function
query=sqlalchemy.select([books.c.genre,sqlalchemy.func.sum(books.c.book_price)]).group_by(books.c.genre).order_by(books.c.genre)
result=engine.execute(query).fetchall()

# view the records
for record in result:
    print("\n",record)

# update
query=books.update().where(books.c.genre=='non-fiction').values(genre='sci-fi')
engine.execute(query)

sql=text('select * from book')
result=engine.execute(sql).fetchall()
# view the records
for record in result:
    print("\n ",record)

# Executing delete query
# syntax from sqlalchemy import delete
#Tablename.delete().where(Tablename.c.column_name == value)

from sqlalchemy import delete
dele = books.delete().where(books.c.genre=='fiction')
engine.execute(dele)

sql=text('select * from book')
result=engine.execute(sql)

# view the record
for record in result:
    print(" \n",record)

# count function
result= sqlalchemy.select([sqlalchemy.func.count()]).select_from(books).scalar()
print("count",result)

query=sqlalchemy.select([books.c.genre,sqlalchemy.func.count(books.c.genre)]).group_by(books.c.genre)
result=engine.execute(query).fetchall()

# view the record
for i in result:
    print("\n ", i)