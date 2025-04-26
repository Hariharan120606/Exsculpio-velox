import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup

urls = [
    "https://www.singaporeair.com",
    "https://www.airfrance.com",
    "https://www.airvistara.com",
    "https://www.garuda-indonesia.com",
    "https://www.cathaypacific.com",
    "https://www.malaysiaairlines.com",
    "https://www.ryanair.com",
    "https://www.vietnamairlines.com",
    "https://www.airasia.com",
    "https://www.thaiairways.com",
]  * 10

semaphore = asyncio.Semaphore(len(urls))  # allow up to 10 concurrent

async def fetch(idx, url, session):
    async with semaphore:
        print(f"Thread {idx} → Fetching {url}")
        t0 = time.time()
        try:
            async with session.get(url, timeout=5) as resp:
                resp.raise_for_status()
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                title = soup.title.string.strip() if soup.title else "N/A"
                print(f"  • Title: {title}")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        finally:
            print(f"Thread {idx} done in {round(time.time() - t0, 2)} s")

async def main():
    start = time.time()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT; Win64; x64)"}
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [
            fetch(i + 1, url, session)
            for i, url in enumerate(urls)
        ]
        await asyncio.gather(*tasks)
    print(f"Parallel completed in: {round(time.time() - start, 2)} s")

if __name__ == "__main__":
    asyncio.run(main())
