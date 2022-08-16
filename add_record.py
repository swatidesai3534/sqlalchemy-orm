from operator import and_
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
from sqlalchemy import Integer,String,Column,MetaData
metadata=MetaData()
from sqlalchemy.orm import declarative_base
Base=declarative_base()
Base.metadata.create_all(engine)
class Customer(Base):
    __tablename__ ="customers"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(30))
    address=Column(String(30))
    email=Column(String(30))
    def __repr__(self):
        return f"Customer(name={self.name!r},address={self.address!r},email={self.email!r})"
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session=sessionmaker()
Session.configure(bind=engine)
session=Session()
c1=Customer(name='Ravi kumar',address='Station Road Nanded',email='Ravi@gmail.com')
session.add(c1)
session.add_all([Customer(name='Komal Pande',address='Koti Hyderabad',email='komal@gmail.com'),
                 Customer(name='Rajendar Nath',address='Sector 40 Gurgaon',email='nath@gmail'),
                 Customer(name='S.M.Krishna',address='Budhwar Peth Pune',email='smk@gmail.com')])
session.commit()

"""result=session.query(Customer).all()
for row in result:
    print("Name=",row.name,"  Address:",row.address,"  Email=",row.email)
x=session.query(Customer).get(2)
print("Name=",x.name,"Address=",x.address,"Email=",x.email)
x.address="Banjara Hills Secunderabad"
session.commit()
x=session.query(Customer).first()
print("Name=",x.name,"Address=",x.address,"Email=",x.email)
x.name='Ravi Shrivastava'
print("Name=",x.name,"Address=",x.address,"Email=",x.email)
session.commit()
session.rollback()
print("Name=",x.name,"Address=",x.address,"Email=",x.email)
session.query(Customer).filter(Customer.id!=2).update({Customer.name:"Mr"+Customer.name},synchronize_session=False)
result=session.query(Customer).filter(Customer.id>2)
for row in result:
    print("name=",row.name," address=",row.address,"email=",row.email)
result=session.query(Customer).one()
for row in result:
    print("name=",row.name," address=",row.address,"email=",row.email)
# equal
result=session.query(Customer).filter(Customer.id==2)
for row in result:
    print("Name:",row.name," address:",row.address," email:",row.email)

# Not equal#
result=session.query(Customer).filter(Customer.id!=2)
for row in result:
    print("ID:",row.id,"name: ",row.name,"address: ",row.address,"email:",row.email)

#Like
result=session.query(Customer).filter(Customer.name.like('Ra%'))
for row in result:
    print("ID:",row.id,"name:",row.name,"address:",row.address,"email:",row.email)

# IN
result=session.query(Customer).filter(Customer.id.in_([1,3]))
for row in result:
    print("ID:",row.id,"Name:",row.name,"address:",row.address,"email:",row.email)
    
# conjunction(multiple condition add by using this method)#
# And
result=session.query(Customer).filter(Customer.id,Customer.name.like('Ra%'))
for row in result:
    print("Id :",row.id,"name:",row.name,"address:",row.address,"email:",row.email)

# _and()
from sqlalchemy import and_
result=session.query(Customer).filter(and_(Customer.id>2,Customer.name.like('Ra%')))
for row in result:
    print("Id:",row.id,"Name:",row.name,"Address:",row.address,"email:",row.email)

# _OR
from sqlalchemy import or_
result=session.query(Customer).filter(or_(Customer.id>2,Customer.name.like('Ra%')))
for row in result:
    print("ID:",row.id,"name:",row.name,"address:",row.address,"email:",row.email)

## Textual SQL
from sqlalchemy import text
cust=session.query(Customer).filter(text("id= :value")).params(value=1).one()
print(cust)

for cust in session.query(Customer).filter(text("id>3")):
    print(cust.name)
from sqlalchemy import text
session.query(Customer).from_statement(text("select * from customers")).all()"""
#print(session.query(Customer).from_statement(text("select * from customers")).all())
from sqlalchemy import text
stmt=text("select name,id,address,email from customers")
stmt=stmt.columns(Customer.id,Customer.name)
print(list(session.query(Customer.id,Customer.name).from_statement(stmt).all()))
