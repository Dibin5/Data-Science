from sqlalchemy import create_engine

msSQL_conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=LAPTOP-OBQA39GB;"
    "DATABASE=test;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# ---------- SQLALCHEMY ENGINE ----------
msSQL_engine = create_engine(
    "mssql+pyodbc://@LAPTOP-OBQA39GB/test"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&encrypt=yes"
    "&trustservercertificate=yes"
)
