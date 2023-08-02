import pandas as pd
num_orders = int(input("Enter the number of orders: "))
order_data ={
    'CustomerID': [],
    'OrderDate': [],
    'ProductName': [],
    'OrderQuantity': []
}
for i in range(num_orders):
    order_data['CustomerID'].append(int(input(f"Enter customer ID for Order {i + 1}: ")))
    order_data['OrderDate'].append(input(f"Enter order date (YYYY-MM-DD) for Order {i + 1}: "))
    order_data['ProductName'].append(input(f"Enter product name for Order {i + 1}: "))
    order_data['OrderQuantity'].append(int(input(f"Enter order quantity for Order {i + 1}: ")))

order_data = pd.DataFrame(order_data)

total_orders_by_customer = order_data['CustomerID'].value_counts()
print("\nTotal number of orders made by each customer:")
print(total_orders_by_customer)

average_order_quantity_per_product = order_data.groupby('ProductName')['OrderQuantity'].mean()
print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)

earliest_order_date = order_data['OrderDate'].min()
latest_order_date = order_data['OrderDate'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
