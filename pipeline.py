from connector import *
from sql import *
from config import *

"""conn = msSQL_conn(msSQL_conn_str)
df = read_database(msSQL_query, conn)
print(df)
"""
# 1. read excel
df = pd.read_excel("global_superstore_2020.xlsx").head(5)
print(df)
# 2. write the excel file into table
table_name = "excel_book"
engine = msSQL_engine
write_database(df, table_name, engine)
# 3. extract data from table
query = msSQL_query
config = msSQL_conn_str
conn = msSQL_conn(config)
df = read_database(query, conn)
print("#######################################")
print(df)
