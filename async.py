import asyncio
import time

async def first_async_func ():
    print("Started first_async_func")
    await asyncio.sleep(2)

async def second_async_func ():
    print("Started second_async_func")
    await asyncio.sleep(4)

print("Start")

async def main():
    task1 = asyncio.create_task(first_async_func())
    task2 = asyncio.create_task(second_async_func())
    await task1
    await task2

asyncio.run(main())
print("Thats all")