import numpy as np

sales_data = np.empty(4)
for quarter in range(4):
    sales_data[quarter] = float(input(f"Enter sales amount for Quarter {quarter + 1}: "))

total_sales_year = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales for the year:", total_sales_year)
print("Percentage increase in sales from the first quarter to the fourth quarter:", percentage_increase, "%")
