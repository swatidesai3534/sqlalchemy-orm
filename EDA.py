

from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import MetaData
metadata_obj=MetaData()
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
mapper_registry=registry()
mapper_registry.metadata
MetaData()
Base=mapper_registry.generate_base()
Base=declarative_base()
class User(Base):
    __tablename__="user_account"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(30))
    fullname=Column(String(30))

    addresses=relationship("Address",back_populates="user",cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r},name={self.name!r},fullname={self.fullname!r})"

class Address(Base):
    __tablename__="address"
    id=Column(Integer,primary_key=True)
    email_address=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    user=relationship("User",back_populates="addresses")

    def __repr__(self):
        return f" Address(id={self.id!r},email_address={self.email_address!r})"

from sqlalchemy.orm import Session
with Session(engine) as session:
    spongebob = User(name="Spongebob",fullname="Spongebob Squarepants",addresses=[Address(email_address="spongebob@sqlachemy.orm")],)
    sandy=User(name="Sandy",fullname="Sandy Cheeks",addresses=[Address(email_address="sandy@sqlalchemy.org"),
                                                               Address(email_address="sandy@squirrelpower.org"),],)
    patrick=User(name="patrick",fullname="Patrick Star")
    session.add_all([spongebob,sandy,patrick])
    session.commit()

from sqlalchemy import select
session = Session(engine)
stmt=select(User).where(User.name.in_(["spongbob","sandy"]))
for user in session.scalars(stmt):
    print(user)
stmt=(select(Address).join(Address.user).where(User.name=="sandy").where(Address.email_address=="sandy@sqlalchemy.org"))
sandy_address=session.scalars(stmt).one()

#make change#
stmt=select(User).where(User.name=="patrick")
patrick=session.scalars(stmt).one()
sandy_address=Address(id=2,email_address='sandy@sqlalchemy.org')
patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
sandy_address.email_address="sandy_cheeks@sqlalchemy.org"
session.commit()
#Some Deletes#
sandy=session.get(User,2)
sandy.addresses.remove(sandy_address)
session.flush()
session.delete(patrick)
session.commit()



