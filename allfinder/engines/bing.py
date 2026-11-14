import urllib.parse
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
name = "bing"

async def search(session, query, filetype="pdf"):
    q = f"{query} filetype:{filetype}"
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q)
    async with session.get(url, headers={"User-Agent": UA}) as r:
        if r.status != 200:
            return []
        soup = BeautifulSoup(await r.text(), "lxml")
    out = []
    for h in soup.select("h2 a"):
        href = h.get("href", "")
        if href.startswith("http"):
            out.append({"url": href, "title": h.get_text(strip=True), "source": name})
    return out
