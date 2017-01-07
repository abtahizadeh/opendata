import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///opendata.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","amir_2016", "Polytechnique", "a.abtahizadeh@polymtl.ca")
session.add(user)
 
# commit the record the database
session.commit()
