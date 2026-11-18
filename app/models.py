from sqlalchemy import String,ForeignKey,Integer,Column

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)

    age = Column(Integer)

    email = Column(String)

    phone = Column(String)


class Role(Base):
    __tablename__ = 'Role'

    role = Column(String)
    role_id = ForeignKey(column=User.id)
    access_department = Column(String)