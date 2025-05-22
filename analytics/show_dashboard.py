import os
from used_cars_cli.analytics.generate_dashboards_plots import generate_dashboard_plots
from used_cars_cli.analytics.generate_summary_report import generate_summary_report

def show_dashboard(conn):
    print("Generating dashboard and summary report...")
    generate_dashboard_plots(conn)
    generate_summary_report(conn)
    print("\n Dashboard and report saved in the 'dashboard_plots' directory.")
    print("Files created:")
    for file in os.listdir("dashboard_plots"):
        print(" -", file)