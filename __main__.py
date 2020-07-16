from Classes.database import Database
from Classes.query import Query
from Classes.funnel import Funnel
from Classes.hypothesis import Hypothesis

if __name__  == '__main__':
    
    # Run the instance of the `Database` class to execute DB setting
    conn = Database.run_database()

    # Make Object from `Query` Class 
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
    
    # Make Obejct from `Funnel` Class
    funnel = Funnel()

    # Get the A_Bfunnel Data in fitness_test_date
    df_AB_fitenss_data = funnel.A_B_fitness_test_Funnel(df)
    funnelA,funnelB = funnel.A_B_fitness_test_Calculate(df)
    print(funnelA)
    print(funnelB)

    # Get the dataframe with `application status`
    df = funnel.A_B_application_Funnel(df)
    app_counts = df.groupby(['ab_test_group', 'is_application']).first_name.count().reset_index()
    

    # Set the pivot table
    app_pivot = app_counts.pivot(columns = 'is_application', index = 'ab_test_group', values = 'first_name').reset_index()

    # Setting the the percentage rate 
    app_pivot['Total'] = app_pivot.Application + app_pivot['No application']
    app_pivot['Application Rate'] = app_pivot.Application / app_pivot.Total

    print(app_pivot)

    # Get the data from app_pivot to execute hypothesis test
    x1 = app_pivot.loc[0, 'Application']
    x2 = app_pivot.loc[0, 'No application']
    x3 = app_pivot.loc[1, 'Application']
    x4 = app_pivot.loc[1, 'No application']

    # Make hypothese object from `Hypothesis` class
    hypothesis = Hypothesis()
    # Execute Chi2 test
    print(hypothesis.contingency(x1,x2,x3,x4))
    pval = hypothesis.contingency(x1,x2,x3,x4)
    # Show the Interpretation
    hypothesis.interpreter(pval)
    

    

    

