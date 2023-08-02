def calculate_total_cost(item_prices, quantities, discount_rate, tax_rate):
    
    total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))

    discount_amount = total_cost_before_discount * (discount_rate / 100)

    total_cost_after_discount = total_cost_before_discount - discount_amount

    tax_amount = total_cost_after_discount * (tax_rate / 100)
    final_total_cost = total_cost_after_discount + tax_amount

    return final_total_cost

item_prices = [float(price) for price in input("Enter item prices separated by spaces: ").split()]
quantities = [int(quantity) for quantity in input("Enter quantities separated by spaces: ").split()]
discount_rate = float(input("Enter discount rate (percentage): "))
tax_rate = float(input("Enter tax rate (percentage): "))

total_cost = calculate_total_cost(item_prices, quantities, discount_rate, tax_rate)

print(f"Total cost for the customer's purchase: ${total_cost:.2f}")
