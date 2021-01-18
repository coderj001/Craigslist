import asyncio
import aiohttp
from bs4 import BeautifulSoup

BASE_URL = "https://huntsville.craigslist.org/search/sss?query="


async def extLink(session, url):
    async with session.get(url) as res:
        html_doc = await res.read()
    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
        img = soup.find('img')
        head = soup.find('span', {'id': 'titletextonly'})
        body = soup.find('section', {'id': 'postingbody'})
        DATA = {
            'head': head.string,
            'img': img['src'],
            'body': body.text[18:130]
        }
        return DATA
    except Exception as e:
        print(e, f"URL: {url}")


async def searching(query):
    url = ''.join((BASE_URL, query))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html_doc = await res.read()
        soup = BeautifulSoup(html_doc.decode('utf-8'), 'html.parser')
        rows = soup.findAll('li', {'class': 'result-row'})
        herfs = list()
        for row in rows:
            try:
                herfs.append(extLink(session, row.find('a')['href']))
            except Exception:
                continue

        return await asyncio.gather(*herfs)
