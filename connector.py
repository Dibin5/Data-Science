from log import *
import pyodbc
import pandas as pd


logger = logging.getLogger()


def msSQL_conn(config):
    logger.info(f"connecting to {config}")
    conn = pyodbc.connect(config)
    return conn


# ---------- READ INTO DATAFRAME ----------
def read_database(query, conn):
    logger.info(f"running this query {query}")
    df = pd.read_sql(query, conn)
    logger.info(df)
    conn.close()
    return df


# ---------- STORE DATAFRAME INTO TABLE ----------
def write_database(df, table_name, engine):
    df.to_sql(
        name=table_name,  # table name
        con=engine,
        if_exists="append",  # append / replace / fail
        index=False,
    )
    logger.info("DataFrame inserted into SQL Server table successfully")
