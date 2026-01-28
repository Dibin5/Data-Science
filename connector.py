import pyodbc
import pandas as pd

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=LAPTOP-OBQA39GB;"
    "DATABASE=test;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str)

# ---------- QUERY ----------
query = """
SELECT TOP (10)
      [Row ID],
      [Order ID],
      [Order Date],
      [Ship Date],
      [Ship Mode],
      [Customer ID],
      [Customer Name]
FROM [test].[dbo].[order_dibin]
"""

# ---------- READ INTO DATAFRAME ----------
df = pd.read_sql(query, conn)
print(df)

conn.close()
