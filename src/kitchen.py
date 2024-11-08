# kitchen.py
import asyncio

SODA_LOCK = asyncio.Lock()
BURGER_SEM = asyncio.Semaphore(3)  # max 3 burgers at a time
FRIES_COUNTER = 0
FRIES_LOCK = asyncio.Lock()

class Kitchen:
    async def get_soda(self):
        async with SODA_LOCK:
            print("    > Filling the soda")
            await asyncio.sleep(1)
            print("    < Soda is ready")

    async def get_burger(self):
        async with BURGER_SEM:
            print("    > Burger ordered in kitchen")
            await asyncio.sleep(3)
            print("    < Burger is ready")

    async def get_fries(self):
        global FRIES_COUNTER
        async with FRIES_LOCK:
            print("    > Getting fries")
            if FRIES_COUNTER == 0:
                print("   ** Starting fry cooking")
                await asyncio.sleep(4)
                FRIES_COUNTER = 5
                print("   ** Fries are cooked")
            FRIES_COUNTER -= 1
            print("    < Fries are ready")
