# main.py
import asyncio
from src.customers import Customer
from src.restaurant import Restaurant

async def main():
    restaurant = Restaurant()
    customers = [Customer(f"Customer {i}") for i in range(5)]
    orders = ["soda", "burger", "fries", "soda", "burger"]

    tasks = [customer.place_order(restaurant, order) for customer, order in zip(customers, orders)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
