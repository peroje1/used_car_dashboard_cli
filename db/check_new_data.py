from used_cars_cli.db.connection import get_connection
from tabulate import tabulate
import pandas as pd
conn = get_connection()
cursor = conn.cursor()

def check_new_data():
    query = "SELECT make, model, year, price, listed_date as date FROM cars ORDER BY id DESC LIMIT 10"
    df = pd.read_sql_query(query, conn)
    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))