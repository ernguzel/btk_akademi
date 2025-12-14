from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///library.db", echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)

SessionLocal = sessionmaker(bind=engine)

# TABLOLARI OLUŞTUR
Base.metadata.create_all(engine)
