# main.py created inside day 96
#  AsyncIO--> Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

import asyncio

async def function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

# async def main():
#     print(await function())
    
async def main():
    L = await asyncio.gather(
            function(),
        )
    print(L)
    
asyncio.run(main())