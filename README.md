# Used Car Listings Dashboard (CLI)

A fully-featured command-line dashboard built in Python for managing and analyzing used car listings. This project simulates a real-world backend system used by dealerships or listing platforms to manage inventory, analyze trends, and make data-driven decisions.

---

## Features

- CLI-based interface for managing car listings.
- Add, filter, and analyze used cars by:
  - Brand
  - Price range
  - Year range
  - City
- Summary analytics (e.g., average price, popular brands, top cities).
- Visualizations using `matplotlib` and `seaborn`.
- Database backend using `SQLite` or configurable via `config.json`.
- Automated dataset generation using `Faker`.

---

## Tech Stack

- **Python 3.10.6**
- **pandas** & **NumPy** – data manipulation
- **matplotlib** & **seaborn** – visualizations
- **SQLAlchemy** – database abstraction
- **SQLite** – default backend (can be configured for Mysql or Postgresql)
- **Faker** – fake data generation
- **JupyterLab/Pycharm / CLI** – development & interaction
(`pip install pandas numpy matplotlib seaborn sqlalchemy faker jupyterlab`)
---
## 1) Configure the Database Connection
- Update the config.json file with your preferred database type.

Example for SQLite (default):
```
{
  "db_type": "sqlite"
}
```
Example for PostgreSQL:
```
{
  "db_type": "postgresql",
  "username": "your_username",
  "password": "your_password",
  "host": "localhost",
  "port": "5432"
}
```
## 2)  Generate Fake Car Listings
- Run the data generator script to create the database and populate it with 1,000 fake used car entries:
`python generate_data_and_database.py`

This will:

- Connect to the database as defined in config.json

- Drop and recreate the cars table

- Populate it with realistic fake car listings using Faker and pandas

## Launch the CLI Dashboard
`python main.py`

You'll be presented with a menu-driven interface to:

- View all listings

- Filter cars by brand, price, city, and year

- Generate and view summary stats and charts

- Add or delete entries

- Exit the program

## Example Output
```
Welcome to the Used Car Dashboard

1. View All Cars
2. Filter Cars
3. Summary Statistics
4. Visualizations
5. Add New Car
6. Delete Car
0. Exit
```



