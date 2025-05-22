import pandas as pd
from tabulate import tabulate
from used_cars_cli.db.connection import get_connection
conn = get_connection()
cursor = conn.cursor()

def get_cheap_cars(max_price=20000):
    query = """
    SELECT make, model, year, price
    FROM cars
    WHERE price < ?
    ORDER BY price ASC
    """
    return pd.read_sql_query(query, conn, params=(max_price,))

def avg_price_by_brand():
    query = """
    SELECT make, ROUND(AVG(price)) AS avg_price
    FROM cars
    GROUP BY make
    ORDER BY avg_price DESC
    """
    return pd.read_sql_query(query, conn)

def most_common_models(limit=10):
    query = """
    SELECT model, COUNT(*) as total_listings
    FROM cars
    GROUP BY model
    ORDER BY total_listings DESC
    LIMIT ?
    """
    return pd.read_sql_query(query, conn, params=(limit,))

def price_by_year():
    query = """
    SELECT year, MIN(price) as min_price, MAX(price) as max_price, AVG(price) as avg_price
    FROM cars
    GROUP BY year
    ORDER BY year ASC
    """
    return pd.read_sql_query(query, conn)

def filter_by_city_and_fuel(city, fuel_type):
    query = """
    SELECT * FROM cars
    WHERE city = ? AND fuel_type = ?
    """
    return pd.read_sql_query(query, conn, params=(city, fuel_type))

def listings_per_month():
    query = """
    SELECT 
        strftime('%Y-%m', listed_date) as month,
        COUNT(*) as total_listings
    FROM cars
    GROUP BY month
    ORDER BY month
    """
    return pd.read_sql_query(query, conn)

def transmission_distribution():
    query = """
    SELECT 
        transmission,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM cars), 2) AS percentage
    FROM cars
    GROUP BY transmission
    ORDER BY percentage DESC
    """
    df = pd.read_sql_query(query, conn)
    print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
    return df
