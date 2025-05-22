from used_cars_cli.filtering.filter_cars import run_cli_filter
from used_cars_cli.analytics.show_dashboard import show_dashboard
from used_cars_cli.analytics.view_data_summaries import view_data_summaries
from used_cars_cli.db.new_car_entry import new_car_entry
from used_cars_cli.db.delete_last_car import delete_last_car
from used_cars_cli.db.check_new_data import check_new_data
from used_cars_cli.db.delete_car_by_id import delete_car_by_id
from used_cars_cli.db.connection import get_connection

conn = get_connection()
cursor = conn.cursor()


def main_menu(conn):
    while True:
        print("\n==== Used Cars CLI Dashboard ====")
        print("1. Filter Cars")
        print("2. Generate Dashboard Summary")
        print("3. View SQL Summary Tables")
        print("4. Add New Car")
        print("5. Delete Last Car")
        print("6. Show Last 10 Cars")
        print("7. Delete Car by ID")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_cli_filter()
        elif choice == "2":
            show_dashboard(conn)
        elif choice == "3":
            view_data_summaries(conn)
        elif choice == "4":
            new_car_entry()
        elif choice == "5":
            delete_last_car()
        elif choice == "6":
            check_new_data()
        elif choice == "7":
            delete_car_by_id()
        elif choice == "0":
            print("Goodbye!")
            cursor.close()
            conn.close()
            break

        else:
            print("Invalid choice. Try again.")

main_menu(conn)
