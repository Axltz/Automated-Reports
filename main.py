import json
from reports.sales_report import generate_sales_report
from reports.inventory_report import generate_inventory_report
from reports.customer_report import generate_customer_report

def load_config():
    with open("config/settings.json", "r") as file:
        return json.load(file)

def main():
    config = load_config()
    output_file = config["output_file"]

    if config["generate_sales_report"]:
        generate_sales_report(
            config["input_files"]["sales"],
            output_file
        )

    if config["generate_inventory_report"]:
        generate_inventory_report(
            config["input_files"]["inventory"],
            output_file
        )

    if config["generate_customer_report"]:
        generate_customer_report(
            config["input_files"]["customers"],
            output_file
        )

    print("Business report generated successfully.")

if __name__ == "__main__":
    main()
