host = "ccs-test-database.caoqx3t4fux5.eu-west-1.rds.amazonaws.com"
database = "ccsdbtest"
user = "postgres"
password = "postgresccs3"
post = "5432"

def select(table_name, conn):
    import pandas as pd
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    return df