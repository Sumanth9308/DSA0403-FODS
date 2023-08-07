import pandas as pd
import numpy as np
from scipy import stats

# Function to calculate the confidence interval
def calculate_confidence_interval(sample_data, confidence_level):
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)  # Using Bessel's correction
    n = len(sample_data)
    t_score = stats.t.ppf(1 - (1 - confidence_level) / 2, df=n - 1)
    margin_of_error = t_score * sample_std / np.sqrt(n)
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Load the customer review data from CSV
data = pd.read_csv('customer_reviews.csv')

# Get user input for the specific product category
product_category = input("Enter the product category for analysis: ")

# Filter data for the specific product category
filtered_data = data[data['product_category'] == product_category]

# Check if the product category exists in the data
if filtered_data.empty:
    print(f"No data available for the product category '{product_category}'.")
    exit()

# Get user input for the confidence level (e.g., 0.95 for 95% confidence level)
while True:
    try:
        confidence_level = float(input("Enter the desired confidence level (between 0 and 1): "))
        if not (0 < confidence_level < 1):
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a valid value between 0 and 1.")

# Calculate the confidence interval for the average rating
rating_ci_lower, rating_ci_upper = calculate_confidence_interval(filtered_data['rating'], confidence_level)

# Output the results
print(f"\nAnalysis for Product Category: {product_category}")
print(f"Average Rating: {filtered_data['rating'].mean():.2f}")
print(f"{confidence_level * 100:.0f}% Confidence Interval for Average Rating: ({rating_ci_lower:.2f}, {rating_ci_upper:.2f})")
