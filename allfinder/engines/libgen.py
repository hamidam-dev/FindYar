import urllib.parse
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
name = "libgen"

MIRRORS = ["https://libgen.is", "https://libgen.rs", "https://libgen.st"]

async def search(session, query, filetype="pdf"):
    for host in MIRRORS:
        try:
            url = f"{host}/search.php?req={urllib.parse.quote(query)}&res=25"
            async with session.get(url, headers={"User-Agent": UA}) as r:
                if r.status != 200:
                    continue
                soup = BeautifulSoup(await r.text(), "lxml")
            out = []
            for row in soup.select("table.c tr"):
                cells = row.find_all("td")
                if len(c
