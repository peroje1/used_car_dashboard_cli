from used_cars_cli.db.connection import get_connection
import pandas as pd
from tabulate import tabulate
from used_cars_cli.analytics.popular_queries import transmission_distribution, listings_per_month

conn = get_connection()

def generate_summary_report(conn):
    with open("dashboard_plots/summary_report.md", "w", encoding="utf-8") as f:
        # Cheap cars
        df = pd.read_sql_query("""
            SELECT make, model, year, price
            FROM cars
            WHERE price < 20000
            ORDER BY price ASC
            LIMIT 10
        """, conn)
        f.write("## Top 10 Cheap Cars Under €20,000\n\n")
        f.write(tabulate(df, headers="keys", tablefmt="github"))
        f.write("\n\n")

        # Most common models
        df2 = pd.read_sql_query("""
            SELECT model, COUNT(*) as total_listings
            FROM cars
            GROUP BY model
            ORDER BY total_listings DESC
            LIMIT 10
        """, conn)
        f.write("## Most Common Car Models\n\n")  # Changed from # to ## for consistency
        f.write(tabulate(df2, headers="keys", tablefmt="github"))
        f.write("\n\n")  # Added extra newline for Markdown formatting

        # Transmission distribution
        df = transmission_distribution()
        f.write("## Transmission Distribution\n\n")
        f.write(tabulate(df, headers="keys", tablefmt="github"))
        f.write("\n\n")

        # Listings per month
        df = listings_per_month()
        f.write("## Listings Per Month\n\n")  # Added newline after header
        f.write(tabulate(df, headers="keys", tablefmt="github"))
        f.write("\n\n")
