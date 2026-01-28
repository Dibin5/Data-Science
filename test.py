from connector import *
from sql import *
from config import *

conn = msSQL_conn(msSQL_conn_str)
df = read_database(msSQL_query, conn)
print(df)

# 1. read excel
# 2. write the excel file into table
# 3. extract data from table
