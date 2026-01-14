import pandas as pd

def generate_customer_report(input_file, output_file):
    df = pd.read_excel(input_file)

    customers_by_country = (
        df.groupby("country")
        .count()
        .reset_index()[["country", "customer_name"]]
        .rename(columns={"customer_name": "total_customers"})
    )

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl",
        mode="a" if _file_exists(output_file) else "w"
    ) as writer:
        df.to_excel(writer, sheet_name="Customer List", index=False)
        customers_by_country.to_excel(
            writer,
            sheet_name="Customers by Country",
            index=False
        )

def _file_exists(path):
    try:
        open(path)
        return True
    except FileNotFoundError:
        return False
