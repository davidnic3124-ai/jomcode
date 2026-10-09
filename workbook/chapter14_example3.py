import asyncio

async def demo():
    await asyncio.sleep(10)
    return "Ready"

print(asyncio.run(demo()))
