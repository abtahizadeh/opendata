from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///opendata.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    ins = Column(String)
    email = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password, ins, email):
        """"""
        self.username = username
        self.password = password
        self.ins = ins
        self.email = email
 
# create tables
Base.metadata.create_all(engine)
