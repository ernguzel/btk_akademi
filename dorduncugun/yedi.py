import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for r in results:
            print(r["title"])

asyncio.run(main())
