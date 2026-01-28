import pandas as pd
from config import *
from log import *

logger = logging.getLogger()

# ---------- READ EXCEL ----------
excel_file = "Book1.xlsx"
df = pd.read_excel(excel_file)

print("DataFrame loaded from Excel:")
print(df.head())


table_name = "Book"
msSQL_write(df, table_name, msSQL_engine)
