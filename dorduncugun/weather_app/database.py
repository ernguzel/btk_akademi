from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite veritabanı
engine = create_engine("sqlite:///weather.db", echo=False)

# ORM Base
Base = declarative_base()

# Session fabrikası
SessionLocal = sessionmaker(bind=engine)
