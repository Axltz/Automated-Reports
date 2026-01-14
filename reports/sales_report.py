import pandas as pd

def generate_sales_report(input_file, output_file):
    df = pd.read_excel(input_file)

    df["total"] = df["quantity"] * df["price"]

    total_sales = df["total"].sum()

    sales_by_product = (
        df.groupby("product")["total"]
        .sum()
        .reset_index()
    )

    sales_by_date = (
        df.groupby("date")["total"]
        .sum()
        .reset_index()
    )

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl",
        mode="a" if _file_exists(output_file) else "w"
    ) as writer:
        df.to_excel(writer, sheet_name="Raw Sales Data", index=False)
        sales_by_product.to_excel(writer, sheet_name="Sales by Product", index=False)
        sales_by_date.to_excel(writer, sheet_name="Sales by Date", index=False)

def _file_exists(path):
    try:
        open(path)
        return True
    except FileNotFoundError:
        return False
