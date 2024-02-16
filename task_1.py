"""task_1.py"""

import asyncio
import json
import os
import aiohttp
import requests

URL = "https://jsonplaceholder.typicode.com/posts"
FOLDER = "json_files"

os.makedirs(FOLDER, exist_ok=True)

resp = requests.get(URL, timeout=10)
json_data = resp.json()

for post in json_data:
    post_id = post["id"]
    filename = f"{FOLDER}/{post_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, indent=4)


async def main():
    """
    main method
    """
    async with aiohttp.ClientSession() as session:
        json_data = await fetch(URL, session)

        for post in json_data:
            post_id = post["id"]
            filename = f"{FOLDER}/{post_id}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(post, f, indent=4)


async def fetch(url, session):
    """async method

    Параметры:
        url (str): URL
        session (): async session

    Возвращает:
        list: json list
    """
    async with session.get(url) as resp:
        return await resp.json()

if __name__ == "__main__":
    asyncio.run(main())
