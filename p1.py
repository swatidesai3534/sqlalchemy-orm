from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:root@localhost:3306/joget")
connection=engine.connect()
from sqlalchemy.orm import declarative_base
Base=declarative_base()
from sqlalchemy import Column,Integer,String
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(30))
    fullname=Column(String(30))
    nickname=Column(String(30))
    def __repr__(self):
        return f"User(name={self.name!r},fullname={self.fullname!r},nickname={self.nickname!r})"
User.__table__
Base.metadata.create_all(engine)
ed_user=User(name='ed',fullname='Ed Jones',nickname='edsnickname')
ed_user.name
#print(ed_user.name)
ed_user.nickname
#print(ed_user.nickname)
str(ed_user.id)
print(str(ed_user.id))