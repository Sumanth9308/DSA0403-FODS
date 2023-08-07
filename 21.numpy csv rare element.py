import pandas as pd
import numpy as np
from scipy import stats

# Function to calculate the sample size needed for a given level of precision
def calculate_sample_size(population_std, confidence_level, precision):
    z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    required_sample_size = (z_score * population_std / precision) ** 2
    return int(np.ceil(required_sample_size))

# Function to calculate the confidence interval
def calculate_confidence_interval(sample_data, confidence_level):
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)  # Using Bessel's correction
    n = len(sample_data)
    z_score = stats.t.ppf(1 - (1 - confidence_level) / 2, df=n - 1)
    margin_of_error = z_score * sample_std / np.sqrt(n)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Load the rare elements concentration data from CSV
data = pd.read_csv('rare_elements.csv')

# Get user input
while True:
    try:
        sample_size = int(input("Enter the sample size: "))
        confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
        precision = float(input("Enter the desired level of precision: "))
        if not (0 < confidence_level < 1):
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter valid values.")

# Randomly select the sample
sample_data = data['concentration'].sample(n=sample_size, random_state=42)

# Calculate the sample mean
sample_mean = np.mean(sample_data)

# Calculate the required sample size for the given precision
population_std = np.std(data['concentration'], ddof=1)  # Using Bessel's correction
required_sample_size = calculate_sample_size(population_std, confidence_level, precision)

# Calculate the confidence interval for the sample mean
lower_bound, upper_bound = calculate_confidence_interval(sample_data, confidence_level)

# Output the results
print(f"\nSample Size: {sample_size}")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Required Sample Size for Desired Precision: {required_sample_size}")
print(f"{confidence_level * 100:.0f}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
