import pandas as pd
from sqlalchemy import create_engine

# ---------- READ EXCEL ----------
excel_file = "global_superstore_2020.xlsx"
df = pd.read_excel(excel_file)

print("DataFrame loaded from Excel:")
print(df.head())

# ---------- SQLALCHEMY ENGINE ----------
engine = create_engine(
    "mssql+pyodbc://@LAPTOP-OBQA39GB/test"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&encrypt=yes"
    "&trustservercertificate=yes"
)

# ---------- STORE DATAFRAME INTO TABLE ----------
df.to_sql(
    name="order_dibin",  # table name
    con=engine,
    if_exists="append",  # append / replace / fail
    index=False,
)

print("DataFrame inserted into SQL Server table successfully")
