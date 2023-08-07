import numpy as np
import scipy.stats as stats

drug_group_data = [120, 122, 118, 125, 121]  

placebo_group_data = [124, 127, 123, 128, 126]  

drug_mean = np.mean(drug_group_data)
drug_std = np.std(drug_group_data, ddof=1)  

placebo_mean = np.mean(placebo_group_data)
placebo_std = np.std(placebo_group_data, ddof=1)

drug_se = drug_std / np.sqrt(len(drug_group_data))
placebo_se = placebo_std / np.sqrt(len(placebo_group_data))

t_value = stats.t.ppf(0.975, df=len(drug_group_data) - 1) 

drug_ci_lower = drug_mean - t_value * drug_se
drug_ci_upper = drug_mean + t_value * drug_se

placebo_ci_lower = placebo_mean - t_value * placebo_se
placebo_ci_upper = placebo_mean + t_value * placebo_se

print("95% Confidence Interval for Mean Reduction in Blood Pressure (Drug Group):")
print(f"Lower Bound: {drug_ci_lower:.2f}")
print(f"Upper Bound: {drug_ci_upper:.2f}\n")

print("95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo Group):")
print(f"Lower Bound: {placebo_ci_lower:.2f}")
print(f"Upper Bound: {placebo_ci_upper:.2f}")
