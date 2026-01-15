# OOP Car Lab (Python)

## Goal

You will practice Object-Oriented Programming by creating a `Car` class with:

-   attributes (model, year, color, for_sale)
-   methods (drive, stop, describe)

Your code must pass the automated tests.

---

## What to Build

### 1) Create a file named `car.py`

In `car.py`, create a class named `Car`.

#### Constructor

Car(model, year, color, for_sale)
It must store all four values as attributes on self:

self.model

self.year

self.color

self.for_sale

2. Add these methods to Car
   All methods must return strings (not print).
   (Tests will check return values.)

drive()
returns: You drive the <color> <model>.

stop()
returns: You stop the <color> <model>.

describe()
returns: <year> <color> <model>

Example:

Car("Mustang", 2024, "red", False).drive() returns
You drive the red Mustang.

3. Create main.py
   In main.py:

import Car

create three cars:

Mustang 2024 red False

Corvette 2025 blue True

Charger 2026 yellow True

print the results of calling drive(), stop(), and describe() for each car

✅ main.py is for demonstration.
✅ The tests grade your Car class.

How to Run Tests
Option A: Run in Codespaces (recommended)

Click Code → Codespaces → Create codespace on main

In the terminal:

pip install -r requirements.txt
pytest

Option B: Run locally
pip install -r requirements.txt
pytest
