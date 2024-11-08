# customers.py
import asyncio
from src.restaurant import Restaurant
from utils.log import Log

class Customer:
    def __init__(self, name, config: dict):
        self.name = name
        self.log = Log("Customer", config)

    async def place_order(self, restaurant, order):
        await restaurant.serve_order(self.name, order)
