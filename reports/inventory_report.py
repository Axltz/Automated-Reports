import pandas as pd

def generate_inventory_report(input_file, output_file):
    df = pd.read_csv(input_file)

    df["status"] = df.apply(
        lambda row: "LOW STOCK" if row["stock"] <= row["min_stock"] else "OK",
        axis=1
    )

    low_stock = df[df["status"] == "LOW STOCK"]

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl",
        mode="a" if _file_exists(output_file) else "w"
    ) as writer:
        df.to_excel(writer, sheet_name="Inventory Status", index=False)
        low_stock.to_excel(writer, sheet_name="Low Stock Alert", index=False)

def _file_exists(path):
    try:
        open(path)
        return True
    except FileNotFoundError:
        return False
