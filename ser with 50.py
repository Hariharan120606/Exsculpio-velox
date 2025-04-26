import time, asyncio, aiohttp
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


sem = asyncio.Semaphore(50)

async def fetch(idx, url, session):
    async with sem:
        print(f"Thread {idx} → Fetching {url}")
        t0 = time.time()
        try:
            async with session.get(url, timeout=5) as resp:
                resp.raise_for_status()
                html = await resp.text()
                title = BeautifulSoup(html, "html.parser").title
                print(f"  • Title: {title.string.strip() if title else 'N/A'}")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        finally:
            print(f"Thread {idx} done in {round(time.time() - t0, 2)} s")

async def main():
    start = time.time()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT; Win64; x64)"}
    async with aiohttp.ClientSession(headers=headers) as session:
        await asyncio.gather(*(fetch(i+1, u, session) for i, u in enumerate(urls)))
    print(f"\nCompleted with 10 threads in {round(time.time() - start, 2)} s")

if __name__ == "__main__":
    asyncio.run(main())
