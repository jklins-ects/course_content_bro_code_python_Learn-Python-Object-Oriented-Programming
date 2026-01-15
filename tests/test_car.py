import pytest
from car import Car


def test_constructor_sets_attributes():
    c = Car("Mustang", 2024, "red", False)
    assert c.model == "Mustang"
    assert c.year == 2024
    assert c.color == "red"
    assert c.for_sale is False


@pytest.mark.parametrize(
    "model,year,color,for_sale,expected_drive,expected_stop,expected_describe",
    [
        ("Mustang", 2024, "red", False,
         "You drive the red Mustang.",
         "You stop the red Mustang.",
         "2024 red Mustang"),
        ("Corvette", 2025, "blue", True,
         "You drive the blue Corvette.",
         "You stop the blue Corvette.",
         "2025 blue Corvette"),
        ("Charger", 2026, "yellow", True,
         "You drive the yellow Charger.",
         "You stop the yellow Charger.",
         "2026 yellow Charger"),
    ]
)
def test_methods_return_expected_strings(model, year, color, for_sale,
                                         expected_drive, expected_stop, expected_describe):
    c = Car(model, year, color, for_sale)

    # Ensure the methods return strings (not None / not print-only)
    drive = c.drive()
    stop = c.stop()
    describe = c.describe()

    assert isinstance(drive, str)
    assert isinstance(stop, str)
    assert isinstance(describe, str)

    assert drive == expected_drive
    assert stop == expected_stop
    assert describe == expected_describe
