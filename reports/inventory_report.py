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


def generate_inventory_report(input_file, output_file):
    df = pd.read_csv(input_file)

    df["stock_status"] = df["quantity"].apply(
        lambda x: "LOW STOCK" if x < 5 else "OK"
    )

    low_stock = df[df["stock_status"] == "LOW STOCK"]

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace"
    ) as writer:

        df.to_excel(writer, sheet_name="Inventory Status", index=False)
        low_stock.to_excel(writer, sheet_name="Low Stock Alerts", index=False)

        for sheet in writer.sheets.values():
            auto_adjust_columns(sheet)
