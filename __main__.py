from Classes.database import Database
from Classes.query import Query
from Classes.funnel import Funnel

if __name__  == '__main__':
    
    # Run the instance of the `Database` class to execute DB setting
    conn = Database.run_database()

    # Make Object the `Query` Class 
    sql_query = Query()

    # Save all data from the 5 table into one dataFrame
    q1 = """SELECT visits.first_name,
                   visits.last_name,
                   visits.visit_date,
                   fitness_tests.fitness_test_date,
                   applications.application_date,
                   purchases.purchase_date
            FROM visits
            LEFT JOIN fitness_tests
                ON fitness_tests.first_name = visits.first_name
                AND fitness_tests.last_name = visits.last_name
                AND fitness_tests.email = visits.email
            LEFT JOIN applications
                ON applications.first_name = visits.first_name
                AND applications.last_name = visits.last_name
                AND applications.email = visits.email
            LEFT JOIN purchases
                ON purchases.first_name = visits.first_name
                AND purchases.last_name = visits.last_name
                AND purchases.email = visits.email
            WHERE visits.visit_date >= '7-1-20'
        """
    # save the the DataFrame where we want to analaze.    
    df = sql_query.sql_query(q1,conn)
    
    # Make Obejct the `Funnel` Class
    funnel = Funnel()
    # Get the A_Bfunnel Data in fitness_test_date
    df_AB_fitenss_data = funnel.A_BFunnel(df)
    print(df_AB_fitenss_data.head())
    funnelA,funnelB = funnel.A_BCalculate(df)
    print(funnelA)
    print(funnelB)

    

    

