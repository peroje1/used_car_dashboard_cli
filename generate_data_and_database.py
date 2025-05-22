import pandas as pd
import random
from faker import Faker
import datetime
import json
from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData, Table

#database config
with open("config.json") as f:
    config = json.load(f)

db_type = config["db_type"]
user = config.get("username", "")
pwd = config.get("password", "")
host = config.get("host", "")
port = config.get("port", "")
db_name = "used_cars"

if db_type == "sqlite":
    conn_str = f"sqlite:///{db_name}.db"
else:
    conn_str = f"{db_type}://{user}:{pwd}@{host}:{port}/{db_name}"

engine = create_engine(conn_str)

#SQL table with auto-incrementing ID
metadata = MetaData()

cars_table = Table("cars", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("make", String),
    Column("model", String),
    Column("year", Integer),
    Column("mileage", Integer),
    Column("condition", String),
    Column("transmission", String),
    Column("fuel_type", String),
    Column("city", String),
    Column("price", Integer),
    Column("dealer", String),
    Column("listed_date", Date)
)

if engine.dialect.has_table(engine.connect(), "cars"):
    cars_table.drop(engine)
cars_table.create(engine)

#Fake data setup
fake = Faker()

brands_models = {
    "Toyota": ["Corolla", "Camry", "Yaris", "RAV4"],
    "Ford": ["Focus", "Fiesta", "Escape", "Fusion"],
    "BMW": ["X3", "X5", "3 Series", "5 Series"],
    "Tesla": ["Model S", "Model 3", "Model X", "Model Y"],
    "Honda": ["Civic", "Accord", "CR-V", "Fit"],
    "Nissan": ["Altima", "Sentra", "Rogue", "Versa"],
    "Audi": ["A3", "A4", "Q5", "Q7"],
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe"],
    "Chevrolet": ["Malibu", "Cruze", "Equinox", "Impala"],
    "Kia": ["Rio", "Soul", "Sportage", "Optima"]
}

conditions = ["excellent", "good", "fair"]
transmissions = ["automatic", "manual"]
fuel_types = ["gasoline", "diesel", "electric", "hybrid"]
cities = ["New York", "Chicago", "Los Angeles", "Houston", "Phoenix",
          "Seattle", "Miami", "Denver", "Atlanta", "San Francisco"]

start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2025, 12, 31)

#Generate fake car data
car_data = []
for _ in range(1000):
    make = random.choice(list(brands_models.keys()))
    model = random.choice(brands_models[make])
    year = random.randint(2010, 2023)
    mileage = random.randint(10000, 150000)
    condition = random.choice(conditions)
    transmission = random.choice(transmissions)
    fuel_type = random.choice(fuel_types)
    city = random.choice(cities)
    price = random.randint(5000, 45000)
    dealer = fake.company()
    listed_date = fake.date_between(start_date=start_date, end_date=end_date)
    car_data.append([
        make, model, year, mileage, condition,
        transmission, fuel_type, city, price, dealer, listed_date
    ])

columns = ["make", "model", "year", "mileage", "condition", "transmission",
           "fuel_type", "city", "price", "dealer", "listed_date"]

df = pd.DataFrame(car_data, columns=columns)

df.to_sql("cars", con=engine, index=False, if_exists="append")

print(df.head())
