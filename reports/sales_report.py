import pandas as pd
from openpyxl.utils import get_column_letter

def auto_adjust_columns(ws):
    for column_cells in ws.columns:
        max_length = 0
        col_letter = get_column_letter(column_cells[0].column)
        for cell in column_cells:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max_length + 2


def generate_sales_report(input_file, output_file):
    df = pd.read_csv(input_file)

    df["date"] = pd.to_datetime(df["date"])
    df["total"] = df["quantity"] * df["price"]

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
        mode="a",
        if_sheet_exists="replace"
    ) as writer:

        df.to_excel(writer, sheet_name="Raw Sales Data", index=False)
        sales_by_product.to_excel(writer, sheet_name="Sales by Product", index=False)
        sales_by_date.to_excel(writer, sheet_name="Sales by Date", index=False)

        for sheet in writer.sheets.values():
            auto_adjust_columns(sheet)
