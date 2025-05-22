import pandas as pd
from tabulate import tabulate
from used_cars_cli.db.connection import get_connection
conn = get_connection()
cursor = conn.cursor()

def delete_car_by_id():
    df = pd.read_sql_query("SELECT id, make, model, year, price, city FROM cars ORDER BY id DESC LIMIT 10", conn)

    if df.empty:
        print("No cars found in the database.")
        conn.close()
        return

    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1  # Start index at 1
    print("\n Last 10 Cars in Database:\n")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

    try:
        car_id = int(input("\nEnter the ID of the car to delete: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        conn.close()
        return

    cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
    car = cursor.fetchone()

    if car:
        confirm = input(f"Are you sure you want to delete car with ID {car_id}? (y/n): ").strip().lower()
        if confirm == "y":
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()
            print(f"Car with ID {car_id} deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No car found with ID {car_id}.")