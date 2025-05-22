from used_cars_cli.db.connection import get_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
conn = get_connection()
cursor = conn.cursor()

def generate_dashboard_plots(conn):
    os.makedirs("dashboard_plots", exist_ok=True)

# Avg price by brand
    df1 = pd.read_sql_query("""
        SELECT make, AVG(price) as avg_price
        FROM cars
        GROUP BY make
        ORDER BY avg_price DESC
        LIMIT 10
    """, conn)

    plt.figure(figsize=(10, 6))
    sns.barplot(x="avg_price", y="make", data=df1, hue="make", legend=False, palette="viridis")
    plt.title("Average Price by Brand")
    plt.xlabel("Average Price (€)")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("dashboard_plots/avg_price_by_brand.png", dpi=300)
    plt.close()

# Price by year
    df2 = pd.read_sql_query("""
        SELECT year, MIN(price) as min_price, MAX(price) as max_price, AVG(price) as avg_price
        FROM cars
        GROUP BY year
        ORDER BY year ASC
    """, conn)

    plt.figure(figsize=(10, 6))
    plt.plot(df2["year"], df2["min_price"], label="Min Price", linestyle='--')
    plt.plot(df2["year"], df2["avg_price"], label="Avg Price", linewidth=2)
    plt.plot(df2["year"], df2["max_price"], label="Max Price", linestyle='--')
    plt.title("Price Range by Year")
    plt.xlabel("Year")
    plt.ylabel("Price (€)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("dashboard_plots/price_by_year.png", dpi=300)
    plt.close()

# Listings per month
    df3 = pd.read_sql_query("""
        SELECT strftime('%Y-%m', listed_date) as month, COUNT(*) as total
        FROM cars
        GROUP BY month
        ORDER BY month
    """, conn)

    plt.figure(figsize=(12, 6))
    sns.barplot(x="month", y="total", data=df3)
    plt.xticks(rotation=45, ha="right")
    plt.title("Listings per Month")
    plt.xlabel("Month")
    plt.ylabel("Total Listings")
    plt.tight_layout()
    plt.savefig("dashboard_plots/listings_per_month.png", dpi=300)
    plt.close()

# Transmission distribution
    df4 = pd.read_sql_query("""
        SELECT transmission, COUNT(*) as count
        FROM cars
        GROUP BY transmission
    """, conn)

    plt.figure(figsize=(6, 6))
    plt.pie(df4["count"], labels=df4["transmission"], autopct='%1.1f%%', startangle=90)
    plt.title("Transmission Distribution")
    plt.tight_layout()
    plt.savefig("dashboard_plots/transmission_distribution.png", dpi=300)
    plt.close()
