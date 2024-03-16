import pandas as pd
import sqlite3

def pysqldf(q, df):
    conn = sqlite3.connect(':memory:')
    df.to_sql('df', conn, if_exists='replace', index=False)
    result = pd.read_sql_query(q, conn)
    conn.close()
    return result
