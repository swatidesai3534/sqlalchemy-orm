from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
from sqlalchemy import String,Integer,Column,ForeignKey,MetaData
metadata_obj=MetaData()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
Base=declarative_base()
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    fullname=Column(String(50))
    nickname=Column(String(30))
    def __repr__(self):
        return f"User(name={self.name!r},fulname={self.fullname!r},nickname={self.nickname!r})"
class Address(Base):
    __tablename__='addresses'
    id=Column(Integer,primary_key=True,autoincrement=True)
    email_address=Column(String(50),nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship("User",back_populates="addresses")
    def __repr__(self):
        return f"Address(email_address={self.email_address!r})"
User.addresses=relationship("Address",order_by=Address.id,back_populates='user')

Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session=sessionmaker()
Session.configure(bind=engine)
session=Session()
jack=User(name='Jack',fullname='Jack Bean',nickname='gjddff')
jack.addresses
jack.addresses=[Address(email_address='jack@google.com'),Address(email_address='j25@yahoo.com')]
jack.addresses[1]
jack.addresses[1].user
session.add(jack)
session.commit()
neck=User(name='neck',fullname='neck pogo',nickname='raju')
neck.addresses
neck.addresses=[Address(email_address='neck@yahoo.com')]
neck.addresses[0]
neck.addresses[0].user
session.add(neck)
session.commit()
### Load the user and addresses entities at once
for u, a in session.query(User,Address).filter(User.id==Address.user_id).filter(Address.email_address=='jack@google.com').all():
    print(u)
    print(a)
session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()