from sqlalchemy import Column, Integer, String, Float
from database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    description = Column(String)
