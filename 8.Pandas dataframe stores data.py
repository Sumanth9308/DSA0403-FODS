import pandas as pd

num_sales = int(input("Enter the number of sales: "))

sales_data = {
    'Product Name': [],
    'Order Quantity': []
}

for i in range(num_sales):
    product_name = input(f"Enter product name for Sale {i + 1}: ")
    order_quantity = int(input(f"Enter order quantity for Sale {i + 1}: "))
    sales_data['Product Name'].append(product_name)
    sales_data['Order Quantity'].append(order_quantity)

sales_df = pd.DataFrame(sales_data)

product_sales = sales_df.groupby('Product Name')['Order Quantity'].sum()

sorted_product_sales = product_sales.sort_values(ascending=False)

top_5_products = sorted_product_sales.head(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
