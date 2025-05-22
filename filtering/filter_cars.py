from used_cars_cli.db.connection import get_connection
from tabulate import tabulate
import pandas as pd
conn = get_connection()
cursor = conn.cursor()


def filter_cars(price_min=None, price_max=None, city=None, make=None, year_min=None, year_max=None):
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    if price_min is not None:
        query += " AND price >= ?"
        params.append(price_min)
    if price_max is not None:
        query += " AND price <= ?"
        params.append(price_max)
    if city:
        query += " AND city = ?"
        params.append(city)
    if make:
        query += " AND make = ?"
        params.append(make)
    if year_min is not None:
        query += " AND year >= ?"
        params.append(year_min)
    if year_max is not None:
        query += " AND year <= ?"
        params.append(year_max)

    query += " ORDER BY price ASC"
    return pd.read_sql_query(query, conn, params=params)


def run_cli_filter():
    print("Car listings filter tool:")

    while True:
        print("\n Apply filters (Press Enter to skip a filter):")

        try:
            price_min = input("Minimum price: ")
            price_min = int(price_min) if price_min.strip() else None

            price_max = input("Maximum price: ")
            price_max = int(price_max) if price_max.strip() else None

            city = input("City: ")
            city = city.strip() if city.strip() else None

            make = input("Brand (Make): ")
            make = make.strip() if make.strip() else None

            year_min = input("Minimum year: ")
            year_min = int(year_min) if year_min.strip() else None

            year_max = input("Maximum year: ")
            year_max = int(year_max) if year_max.strip() else None

            print("\n Filtering results...\n")
            df = filter_cars(price_min, price_max, city, make, year_min, year_max)

            if df.empty:
                print(" No results found with the given filters.")
            else:
                print(tabulate(df.head(20), headers='keys', tablefmt='pretty', showindex=False))
                print(f"\n {len(df)} results found.")

                export = input(" Export results to CSV? (y/n): ").lower()
                if export == "y":
                    filename = input("Enter filename (e.g., results.csv): ").strip()
                    if not filename.endswith(".csv"):
                        filename += ".csv"
                    df.to_csv(filename, index=False)
                    print(f" Exported to {filename}")

        except ValueError:
            print("Invalid input. Please enter numbers.")

        again = input("\n Filter again? (y/n): ").lower()
        if again != "y":
            print(" Exiting filter tool. Goodbye!")
            break
