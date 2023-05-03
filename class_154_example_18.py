from asyncio import run, gather
from httpx import AsyncClient

base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def download(number):    
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number),
            timeout=None
        )
        print(number, response.json()['name'])
        return number, response.json()['name']


async def coro(start, stop):
    return await gather(
        *[download(number) for number in range(start, stop)],
    )


from pprint import pprint
result = run(coro(1, 5))
pprint(result)