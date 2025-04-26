import time
import requests
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

start = time.time()
for idx, url in enumerate(urls, 1):
    print(f"Thread {idx} → Fetching {url}")
    try:
        resp = requests.get(
            url,
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT; Win64; x64)"
            }
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "N/A"
        print(f"  • Title: {title}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
print(f"Serial completed in: {round(time.time() - start, 2)} s")
