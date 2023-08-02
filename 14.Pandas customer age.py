from collections import defaultdict

def get_customer_age_distribution(purchase_data):
    age_distribution = defaultdict(int)

    for purchase in purchase_data:
        age = purchase.get("age")
        if age is not None:
            age_distribution[age] += 1

    return age_distribution

purchase_data = []
num_customers = int(input("Enter the number of customers: "))

for i in range(num_customers):
    name = input(f"Enter the name of customer {i+1}: ")
    age = int(input(f"Enter the age of customer {i+1}: "))
    purchase_data.append({"name": name, "age": age})

age_distribution = get_customer_age_distribution(purchase_data)

print("\nAge Distribution of Customers:")
for age, count in age_distribution.items():
    print(f"Age {age}: {count} customers")
