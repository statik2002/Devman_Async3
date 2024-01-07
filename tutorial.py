import asyncio
import time
from datetime import datetime


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


asyncio.run(main())
