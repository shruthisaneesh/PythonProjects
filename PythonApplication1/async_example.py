import asyncio
import time

async def a():
    await asyncio.sleep(7)
    print('testing A...')

async def b():
    await asyncio.sleep(2)
    print('testing B...')

async def main():
    task1 = asyncio.create_task(a())
    await b()
    await task1

start =time.time()
asyncio.run(main())
print(f"time after completion: ", (time.time() - start))
