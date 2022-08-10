import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
# Declare mapping
from sqlalchemy.orm import declarative_base
Base=declarative_base()
from sqlalchemy import Column,String,Integer
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    fullname=Column(String(50))
    nickname=Column(String(30))
    def __repr__(self):
        return f"User(name={self.name!r},fulname={self.fullname!r},nickname={self.nickname!r})"
# Create a Schema¶
User.__table__
print(User.__table__)
from sqlalchemy.orm import sessionmaker
Session=sessionmaker()
Session.configure(bind=engine)
session=Session()
#Adding and Updating Objects¶
ed_user=User(name='ed',fullname='ED Jones',nickname='edsnickname')
session.add(ed_user)
#session.commit()
our_user=session.query(User).filter_by(name='ed').first()
our_user
#print(ed_user is our_user)
session.add_all([User(name='wendy',fullname='Wendy Williams',nickname='Windy'),
                 User(name='mary',fullname='Mary Contrary',nickname='mary'),
                 User(name='fred',fullname='Fried Flintstone',nickname='Freddy')])
#session.commit()
# chnage nickname 'ed'..#
ed_user.nickname='eddie'
session.dirty
session.new
session.commit()
ed_user.id
print(ed_user.id)
# Rolling back #
ed_user.name='Edwardo'
session.add(ed_user)
#session.commit()
#print(ed_user.name)
fake_user=User(name='fakeuser',fullname='Invalid',nickname='12345')
session.add(fake_user)
#session.commit()
session.query(User).filter(User.name.in_(['Edwardo','fakeuser'])).all()
session.rollback()
ed_user.name
print(ed_user)
#session.commit()
fake_user in session
print(fake_user in session)
# Querying#
for instance in session.query(User).order_by(User.id):
    print(instance.name,instance.fullname)

for name,fullname in session.query(User.name,User.fullname):
    print(name,fullname)