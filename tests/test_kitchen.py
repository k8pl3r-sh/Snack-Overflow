# tests/test_kitchen.py
import unittest
from unittest.mock import AsyncMock, patch
from src.kitchen import Kitchen

class TestKitchen(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.kitchen = Kitchen()
        self.kitchen.get_soda = AsyncMock()
        self.kitchen.get_fries = AsyncMock()
        self.kitchen.get_burger = AsyncMock()

    async def test_get_soda(self):
        await self.kitchen.get_soda()
        self.kitchen.get_soda.assert_awaited_once()
        self.kitchen.get_burger.assert_not_awaited()
        self.kitchen.get_fries.assert_not_awaited()

if __name__ == "__main__":
    unittest.main()