# First we need the asyncio library
import asyncio

# We also need something to run
async def main():
    for char in 'Hello, world!\n':
        print(char, end='', flush=True)
        await asyncio.sleep(0.2)

# Then, we can create a new asyncio loop and use it to run our coroutine.
# The creation and tear-down of the loop is hidden away from us.
asyncio.run(main())