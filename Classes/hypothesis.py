from scipy.stats import chi2_contingency

class Hypothesis:
    chi2 = 0.0
    pval = 0.0
    dof = 0.0
    expected = ""

    def contingency(self,x1,x2,x3,x4):
        contingency = [[x1,x2],
                       [x3,x4]]

        chi2, pval, dof, expected = chi2_contingency(contingency)

        return pval
    
    def interpreter(self,pval):
        if pval < 0.05:
            print("P-value is less than 0.05. This means that the difference is significant.")
        else:
            print("P-value is higher than 0.05. This means that theire is no difference between A and B Group")