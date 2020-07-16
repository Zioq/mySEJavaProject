import pandas as pd

class Query():

    query = ""
    conn = ""
    def sql_query(self,query,conn):
        try:
            df = pd.read_sql(query, conn)
        except Exception as e:
            print(e.message)
        return df


    

    