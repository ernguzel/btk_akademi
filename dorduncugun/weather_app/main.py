import asyncio
from database import Base, engine
from services.weather_service import WeatherService
from repository.weather_repository import WeatherRepository

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

async def run():
    service = WeatherService(WeatherRepository())

    print("Hava durumu alınıyor...")
    await service.fetch_and_save("Istanbul")

    print("\nKayıtlı hava durumu verileri:")
    for w in service.list_records():
        print(f"{w.city} | {w.temperature}°C | {w.description}")

asyncio.run(run())
