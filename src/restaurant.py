# restaurant.py
import asyncio
from src.kitchen import Kitchen

class Restaurant:
    def __init__(self, config: dict):
        self.kitchen = Kitchen(config)

    async def serve_order(self, customer_name, order):
        print(f"{customer_name} has ordered: {order}")
        if order == "soda":
            await self.kitchen.get_soda()
        elif order == "burger":
            await self.kitchen.get_burger()
        elif order == "fries":
            await self.kitchen.get_fries()
        else:
            print(f"{order} is not on the menu!")
