# Snack-Overflow
Python project for university

#### Architecture

```
fast_food_simulation/
│
├── main.py                      # Main application entry point
├── config.yml                   # Config for client generator
├── config_food.yml              # Dynamic config for food stockpile
├── restaurant.py                # Restaurant class with menu items
├── customers.py                 # Customer class with order handling
├── suppliers.py                 # Supplier class for buying furnitures
├── kitchen.py                   # Kitchen class for food preparation
├── customers_generator.py       # Way to create customers with orders

├── tests/                       # Unit tests for the application
│   ├── __init__.py
│   ├── test_restaurant.py
│   ├── test_customers.py
│   └── test_kitchen.py
└── requirements.txt     # Project dependencies

```

#### To implement
- Multithreading (with/without GIL)
- design pattern to implement : https://refactoring.guru/design-patterns/python
- decorators (to be better on it)
- unit tests
