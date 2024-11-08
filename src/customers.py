# customers.py
import asyncio
from src.restaurant import Restaurant

class Customer:
    def __init__(self, name):
        self.name = name

    async def place_order(self, restaurant, order):
        await restaurant.serve_order(self.name, order)
