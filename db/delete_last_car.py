import pandas as pd
from used_cars_cli.db.connection import get_connection
conn = get_connection()
cursor = conn.cursor()

def delete_last_car():
    cursor.execute("""
        SELECT id
        FROM cars
        ORDER BY id DESC
        LIMIT 1;
    """)
    last_car_id = cursor.fetchone()

    if last_car_id:
        cursor.execute("""
            DELETE FROM cars
            WHERE id = ?;
        """, (last_car_id[0],))
        conn.commit()
        print(f"Car with ID {last_car_id[0]} deleted successfully.")
    else:
        print("No cars found to delete.")