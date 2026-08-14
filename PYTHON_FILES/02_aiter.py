# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 02 - aiter
# Companion digitale - esempio principale

import asyncio

async def numeri():
    yield 10
    yield 20

async def main():
    it = aiter(numeri())
    print(await anext(it))

asyncio.run(main())
