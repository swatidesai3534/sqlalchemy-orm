"""import csv
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import insert
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
connection=engine.connect()
#sql='select * from demo'
data=connection.execute(text("select *from demo"))
print(data.all())"""


from sqlalchemy import create_engine,ForeignKey,Column,Integer,String
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
from sqlalchemy.orm import relationship
class Customer(Base):
    __tablename__='customers'
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    address=Column(String(50))
    email=Column(String(50))

class Invoice(Base):
    __tablename__='invoices'
    id=Column(Integer,primary_key=True)
    custid=Column(Integer,ForeignKey('customers.id'))
    invno=Column(Integer)
    amount=Column(Integer)
    customer=relationship("Customer",back_populates="invoices")
Customer.invoices=relationship("Invoice",order_by=Invoice.id,back_populates="customer")
Base.metadata.create_all(engine)
c1=Customer(name="Gopal Krishna",address="Bank Street Hydarebad",email="gk@gmail.com")
c1.invoices=[Invoice(invno=10,amount=15000),Invoice(invno=14,amount=3850)]
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()
session.add(c1)
session.commit()
c2=Customer(name="Govind pant",address="Gulmandi Aurangabad",email="gpant@gmail.com",invoices=[Invoice(invno=3,amount=10000),Invoice(invno=4,amount=5000)])
c2.invoices=[Invoice(invno=3,amount=10000),Invoice(invno=4,amount=5000)]
session.add(c2)
session.commit()
row=[Customer(name="Govind Kala",address="Gulmandi Aurangabad",email='kala@gmail.com',invoices=[Invoice(invno=7,amount=12000),Invoice(invno=8,amount=18500)]),Customer(name="Abdul Rahman",address="Rhotak",email="abdulr@gmail.com",invoices=[Invoice(invno=9,amount=15000),Invoice(invno=11,amount=6000)])]
session.add_all(row)
session.commit()
##JOINS##
for c,i in session.query(Customer,Invoice).filter(Customer.id==Invoice.custid).all():
    print("ID: {}Name: {} Invoice NO: {} Amount: {}".format(c.id,c.name,i.invno,i.amount))

print(session.query(Customer).join(Invoice).filter(Invoice.amount==8500).all())

# by using for loop
result=session.query(Customer).join(Invoice).filter(Invoice.amount==8500)
for row in result:
    for inv in invoices:
        print(row.id,row.name,inv.invno,inv.amount)


