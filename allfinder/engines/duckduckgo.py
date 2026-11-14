import urllib.parse
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
name = "duckduckgo"

@retry(stop=stop_after_attempt(2), wait=wait_exponential(min=1, max=4))
async def search(session, query, filetype="pdf"):
    q = f"{query} filetype:{filetype}"
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    async with session.get(url, headers={"User-Agent": UA}) as r:
        if r.status != 200:
            return []
        soup = BeautifulSoup(await r.text(), "lxml")
    out = []
    for a in soup.select("a.result__a"):
        href = a.get("href", "")
        if href:
            out.append({"url": href, "title": a.get_text(strip=True), "source": name})
    return out
