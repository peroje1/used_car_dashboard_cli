from used_cars_cli.db.connection import get_connection
conn = get_connection()
cursor = conn.cursor()

def add_new_car(make, model, year, mileage, condition,
                transmission, fuel_type, city, price, dealer, listed_date):

    query = """
    INSERT INTO cars (
        make, model, year, mileage, condition,
        transmission, fuel_type, city, price, dealer, listed_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = (make, model, year, mileage, condition,
              transmission, fuel_type, city, price, dealer, listed_date)

    cursor.execute(query, values)
    conn.commit()