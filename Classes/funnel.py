import pandas as pd

class Funnel:

    funnelA = 0
    funnelB = 0

    # Design the Funnel to use A/B Test
    def A_BFunnel(self,df):
        df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B')
        
        return df
    
    def A_BCalculate(self,df):
        count_A = df[df.ab_test_group =='A']
        funnelA = len(count_A)
        count_B = df[df.ab_test_group == 'B']
        funnelB = len(count_B)
        return funnelA,funnelB
        #print(funnelA)
        #print(funnelB)