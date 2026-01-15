from car import Car


def main():
    car1 = Car("Mustang", 2024, "red", False)
    car2 = Car("Corvette", 2025, "blue", True)
    car3 = Car("Charger", 2026, "yellow", True)

    cars = [car1, car2, car3]

    for c in cars:
        print(c.drive())
        print(c.stop())
        print(c.describe())
        print("-" * 20)


if __name__ == "__main__":
    main()
