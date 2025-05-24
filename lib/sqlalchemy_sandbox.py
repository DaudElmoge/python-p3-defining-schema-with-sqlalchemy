#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):#Student is a Python class that represents a table named students.
    __tablename__ = "students"#__tablename__ = 'students' tells SQLAlchemy what to call the actual table
    id =Column(Integer(),primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine ("sqlite:///students.db")
    Base.metadata.create_all(engine)#create_engine('sqlite:///students.db') creates a connection to a new (or existing) SQLite file-based database called students.db.
    #This block runs only when the script is executed directly (python lib/sqlalchemy_sandbox.py).