# kitchen.py
import asyncio
from utils.log import Log


class Kitchen:
    def __init__(self, config: dict):
        self.SODA_LOCK = asyncio.Lock()
        self.BURGER_LOCK = asyncio.Semaphore(3)
        self.FRIES_LOCK = asyncio.Lock()
        self.FRIES_COUNTER = 0
        self.log = Log("Kitchen", config)

    async def get_soda(self):
        async with self.SODA_LOCK:
            self.log.info(f"    > Filling the soda")
            await asyncio.sleep(1)
            self.log.info(f"    < Soda is ready")


    async def get_burger(self):

        async with self.BURGER_LOCK:
            self.log.info(f"    > Burger ordered in kitchen")
            print("")
            await asyncio.sleep(3)
            print("    < Burger is ready")

    async def get_fries(self):
        async with self.FRIES_LOCK:
            print("    > Getting fries")
            if self.FRIES_COUNTER == 0:
                print("   ** Starting fry cooking")
                await asyncio.sleep(4)
                self.FRIES_COUNTER = 5
                print("   ** Fries are cooked")
            self.FRIES_COUNTER -= 1
            print("    < Fries are ready")
