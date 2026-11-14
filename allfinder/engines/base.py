from typing import Protocol

class Engine(Protocol):
    name: str
    async def search(self, session, query: str, filetype: str) -> list[dict]: ...
