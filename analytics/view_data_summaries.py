from used_cars_cli.db.connection import get_connection
from tabulate import tabulate
import pandas as pd
conn = get_connection()
cursor = conn.cursor()


def view_data_summaries(conn):
    while True:
        print("\n==== View Data Summaries ====")
        print("1. Top 10 Brands by Average Price (with search)")
        print("2. Price Range by Year (with sort)")
        print("3. Listings per Month (with sort)")
        print("4. Transmission Distribution (with filter)")
        print("5. Cheapest Cars (filter by price range)")
        print("6. Most Common Models (with sort)")
        print("0. Back to Main Menu")

        choice = input("Choose a summary to view: ")

        if choice == "1":
            keyword = input("Search brand name (press Enter to skip): ").strip()
            query = """
                SELECT make, ROUND(AVG(price), 2) as avg_price
                FROM cars
                GROUP BY make
            """
            df = pd.read_sql_query(query, conn)
            if keyword:
                df = df[df["make"].str.contains(keyword, case=False, na=False)]
            df = df.sort_values("avg_price", ascending=False).head(10)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "2":
            sort_option = input("Sort by (min_price / avg_price / max_price): ").strip().lower()
            if sort_option not in ["min_price", "avg_price", "max_price"]:
                sort_option = "avg_price"
            query = f"""
                SELECT year, MIN(price) as min_price, MAX(price) as max_price, ROUND(AVG(price), 2) as avg_price
                FROM cars
                GROUP BY year
                ORDER BY {sort_option} DESC
            """
            df = pd.read_sql_query(query, conn)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "3":
            order = input("Sort total listings by (asc/desc): ").strip().lower()
            if order not in ["asc", "desc"]:
                order = "desc"
            query = f"""
                SELECT strftime('%Y-%m', listed_date) as month, COUNT(*) as total_listings
                FROM cars
                GROUP BY month
                ORDER BY total_listings {order.upper()}
            """
            df = pd.read_sql_query(query, conn)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "4":
            filter_trans = input("Enter transmission type to filter (press Enter to skip): ").strip()
            query = """
                SELECT transmission, COUNT(*) as count
                FROM cars
                GROUP BY transmission
            """
            df = pd.read_sql_query(query, conn)
            if filter_trans:
                df = df[df["transmission"].str.contains(filter_trans, case=False, na=False)]
            df = df.sort_values("count", ascending=False)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "5":
            try:
                min_price = int(input("Minimum price (default 0): ") or "0")
                max_price = int(input("Maximum price (default 20000): ") or "20000")
            except ValueError:
                min_price, max_price = 0, 20000
            query = f"""
                SELECT make, model, year, price
                FROM cars
                WHERE price BETWEEN {min_price} AND {max_price}
                ORDER BY price ASC
                LIMIT 10
            """
            df = pd.read_sql_query(query, conn)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "6":
            order = input("Sort by total listings (asc/desc): ").strip().lower()
            if order not in ["asc", "desc"]:
                order = "desc"
            query = f"""
                SELECT model, COUNT(*) as total_listings
                FROM cars
                GROUP BY model
                ORDER BY total_listings {order.upper()}
                LIMIT 10
            """
            df = pd.read_sql_query(query, conn)
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")