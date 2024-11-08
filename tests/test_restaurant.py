# tests/test_restaurant.py
import unittest
from unittest.mock import AsyncMock, patch
from src.restaurant import Restaurant


class TestRestaurant(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        # Setup the Restaurant instance with a mocked Kitchen
        self.restaurant = Restaurant()
        self.restaurant.kitchen.get_soda = AsyncMock()
        self.restaurant.kitchen.get_burger = AsyncMock()
        self.restaurant.kitchen.get_fries = AsyncMock()

    async def test_serve_order_soda(self):
        # Test that serve_order calls get_soda when ordering "soda"
        await self.restaurant.serve_order("Alice", "soda")
        self.restaurant.kitchen.get_soda.assert_awaited_once()
        self.restaurant.kitchen.get_burger.assert_not_awaited()
        self.restaurant.kitchen.get_fries.assert_not_awaited()

    async def test_serve_order_burger(self):
        # Test that serve_order calls get_burger when ordering "burger"
        await self.restaurant.serve_order("Bob", "burger")
        self.restaurant.kitchen.get_burger.assert_awaited_once()
        self.restaurant.kitchen.get_soda.assert_not_awaited()
        self.restaurant.kitchen.get_fries.assert_not_awaited()

    async def test_serve_order_fries(self):
        # Test that serve_order calls get_fries when ordering "fries"
        await self.restaurant.serve_order("Charlie", "fries")
        self.restaurant.kitchen.get_fries.assert_awaited_once()
        self.restaurant.kitchen.get_soda.assert_not_awaited()
        self.restaurant.kitchen.get_burger.assert_not_awaited()

    async def test_serve_order_invalid_item(self):
        # Test that serve_order does nothing for an invalid order
        with patch("builtins.print") as mock_print:
            await self.restaurant.serve_order("David", "pasta")
            mock_print.assert_called_with("pasta is not on the menu!")

        # Ensure no kitchen methods were called
        self.restaurant.kitchen.get_soda.assert_not_awaited()
        self.restaurant.kitchen.get_burger.assert_not_awaited()
        self.restaurant.kitchen.get_fries.assert_not_awaited()


# Run the tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
