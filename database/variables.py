from .models import *

host = "ccs-test-database.caoqx3t4fux5.eu-west-1.rds.amazonaws.com"
database = "ccsdbtest"
user = "postgres"
password = "postgresccs3"
post = "5432"

data_dic = {
    'exemple_personnels': exemple_personnels
}

list_vues = data_dic.keys()

def list_tuple(list):
    tuple_list = [] 
    for ele in list_vues:
        tuple = (ele, ele)
        tuple_list.append(tuple)
    return tuple_list

def select(table_name, conn):
    import pandas as pd
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    return df

