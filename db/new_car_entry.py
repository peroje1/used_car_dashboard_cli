from used_cars_cli.db.connection import get_connection
import datetime
from used_cars_cli.db.add_new_car import add_new_car
conn = get_connection()
cursor = conn.cursor()

def get_valid_date(prompt="Enter listed date (YYYY/MM/DD): "):
    while True:
        listed_date_input = input(prompt).strip()
        try:
            listed_date = datetime.datetime.strptime(listed_date_input, "%Y/%m/%d").date()
            if listed_date > datetime.date.today():
                print("Listed date cannot be in the future.")
            elif listed_date < datetime.date(1950, 1, 1):
                print("Date is too old (before 1950).")
            else:
                return listed_date
        except ValueError:
            print("Invalid date format, must use YYYY/MM/DD.")

def new_car_entry():
    print("Please enter the car details:\n")

    make = input("Enter car brand: ").strip().title()
    model = input("Enter car model: ").strip().title()

    while True:
        try:
            year = int(input("Enter car production year: "))
            if year < 1950 or year > datetime.datetime.now().year:
                raise ValueError
            break
        except ValueError:
            print("Year must be between 1950 and now.")

    while True:
        try:
            mileage = int(input("Enter car mileage: "))
            if mileage < 0 or mileage > 1_000_000:
                raise ValueError
            break
        except ValueError:
            print("Mileage must be between 0 and 1,000,000.")

    valid_condition = ["excellent", "good", "fair"]
    while True:
        condition = input("Condition (excellent/good/fair): ").strip().lower()
        if condition in valid_condition:
            break
        print(f"Condition must be one of {valid_condition}.")

    valid_transmission = ["automatic", "manual"]
    while True:
        transmission = input("Transmission (automatic/manual): ").strip().lower()
        if transmission in valid_transmission:
            break
        print(f"Transmission must be one of {valid_transmission}.")

    valid_fuels = ["gasoline", "diesel", "electric", "hybrid"]
    while True:
        fuel_type = input("Fuel type (gasoline/diesel/electric/hybrid): ").strip().lower()
        if fuel_type in valid_fuels:
            break
        print(f"Fuel type must be one of {valid_fuels}.")

    city = input("Enter city: ").strip().title()

    while True:
        try:
            price = int(input("Price: "))
            if price < 0 or price > 1_000_000:
                raise ValueError
            break
        except ValueError:
            print("Price must be between 0 and 1,000,000.")

    dealer = input("Enter dealer name: ").strip().title()

    listed_date = get_valid_date()

    add_new_car(
        make, model, year, mileage, condition,
        transmission, fuel_type, city, price, dealer, listed_date.isoformat()
    )

    print("\n New car added successfully!\n")