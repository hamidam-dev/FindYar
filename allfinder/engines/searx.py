import os, urllib.parse
import aiohttp

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
name = "searx"

async def search(session, query, filetype="pdf"):
    inst = os.getenv("SEARX_INSTANCE", "https://searx.be")
    url = f"{inst}/search?q={urllib.parse.quote(query)}&format=json&categories=files"
    try:
        async with session.get(url, headers={"User-Agent": UA}, timeout=aiohttp.ClientTimeout(total=15)) as r:
            if r.status != 200:
                return []
            data = await r.json(content_type=None)
    except Exception:
        return []
    return [
        {"url": x["url"], "title": x.get("title", ""), "source": name}
        for x in data.get("results", [])
    ]
