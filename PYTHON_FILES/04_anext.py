# PYTHON: 71 FUNZIONI DA CAPIRE E USARE
# Scheda 04 - anext
# Companion digitale - esempio principale

import asyncio

async def dati():
    yield "A"

async def main():
    it = aiter(dati())
    print(await anext(it))
    print(await anext(it, "fine"))

asyncio.run(main())
