import numpy as np

def get_sales_data():
    print("Enter the sales data for each product (3x3 matrix)")
    sales_data = []
    for i in range(3):
        row = input(f"Enter sales data for product {i+1} (separated by spaces): ")
        sales_data.append([int(x) for x in row.split()])
    return np.array(sales_data)

def main():
    
    sales_data = get_sales_data()

    average_price = np.mean(sales_data)

    print("Average Price of all products sold in the past month:", average_price)

if __name__ == "__main__":
    main()

