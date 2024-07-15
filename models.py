#  defining your database models

# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"  # Replace with your local PostgreSQL details

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Chore(Base):
    __tablename__ = "chores"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True, index=True)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    week_number = Column(Integer, index=True)
    person_id = Column(Integer, ForeignKey("people.id"))
    chore_id = Column(Integer, ForeignKey("chores.id"))
    person = relationship("Person")
    chore = relationship("Chore")
