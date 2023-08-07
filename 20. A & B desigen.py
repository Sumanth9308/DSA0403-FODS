import numpy as np
import scipy.stats as stats

design_a_conversion_rates = [0.12, 0.15, 0.10, 0.14, 0.18]  
design_b_conversion_rates = [0.09, 0.11, 0.08, 0.10, 0.12]  

t_statistic, p_value = stats.ttest_ind(design_a_conversion_rates, design_b_conversion_rates)

alpha = 0.05

if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and website design B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and website design B.")
