from models.weather import Weather
from repository.weather_repository import WeatherRepository
from api.weather_api import fetch_weather

class WeatherService:
    def __init__(self, repo: WeatherRepository):
        self.repo = repo

    async def fetch_and_save(self, city: str):
        data = await fetch_weather()

        weather = Weather(
            city=city,
            temperature=data["temperature"],
            description=data["description"]
        )

        return self.repo.add(weather)

    def list_records(self):
        return self.repo.list()
