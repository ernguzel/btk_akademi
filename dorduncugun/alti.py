import asyncio

async def greet():
    print("Merhaba!")
    await asyncio.sleep(1)
    print("1 saniye sonra: Selam tekrar!")

asyncio.run(greet())
