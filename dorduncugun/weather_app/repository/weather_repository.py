from database import SessionLocal
from models.weather import Weather

class WeatherRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add(self, weather: Weather):
        self.db.add(weather)
        self.db.commit()          #  VERİ KALICI OLUR
        self.db.refresh(weather)
        return weather

    def list(self):
        return self.db.query(Weather).all()
