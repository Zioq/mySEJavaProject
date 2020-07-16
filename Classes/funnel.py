import pandas as pd

class Funnel:

    fitness_test_funnelA = 0
    fitness_test_funnelB = 0

    # Design the Funnel to use A/B Test
    def A_B_fitness_test_Funnel(self,df):
        df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B')
        
        return df
    
    def A_B_fitness_test_Calculate(self,df):
        count_A = df[df.ab_test_group =='A']
        fitness_test_funnelA = len(count_A)
        count_B = df[df.ab_test_group == 'B']
        fitness_test_funnelB = len(count_B)
        return fitness_test_funnelA,fitness_test_funnelB

    def A_B_application_Funnel(self,df):
        df['is_application'] = df.application_date.apply(lambda x: 'Application' if pd.notnull(x) else 'No application')

        return df
    
    
