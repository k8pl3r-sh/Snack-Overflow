# main.py
import asyncio
from src.customers import Customer
from src.restaurant import Restaurant
from yaml import safe_load

async def main():
    config = safe_load(open("config.yml"))
    restaurant = Restaurant(config)
    customers = [Customer(f"Customer {i}", config) for i in range(5)]
    orders = ["soda", "burger", "fries", "soda", "burger"]

    tasks = [customer.place_order(restaurant, order) for customer, order in zip(customers, orders)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
