import os
from config import CONFIG
from reports.sales_report import generate_sales_report
from reports.inventory_report import generate_inventory_report

def main():
    input_sales = CONFIG["input_files"]["sales"]
    input_inventory = CONFIG["input_files"]["inventory"]

    output_dir = CONFIG["output_dir"]
    output_file = os.path.join(output_dir, CONFIG["output_file"])

    os.makedirs(output_dir, exist_ok=True)

    # Crear Excel (ventas)
    generate_sales_report(input_sales, output_file)

    # Agregar inventario al mismo Excel
    generate_inventory_report(input_inventory, output_file)

    print("Business report generated successfully:", output_file)

if __name__ == "__main__":
    main()
