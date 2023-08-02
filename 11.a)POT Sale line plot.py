import matplotlib.pyplot as plt

def create_line_plot(months, sales):
   
    plt.plot(months, sales, marker='o', color='b')
    plt.xlabel('Months')
    plt.ylabel('Sales')
    plt.title('Monthly Sales')
    plt.grid(True)
    plt.show()

def get_input_data():
    months = []
    sales = []

    for i in range(1, 4):
        month = input(f"Enter the name of month {i}: ")
        sales_amount = int(input(f"Enter the sales amount for {month}: "))
        months.append(month)
        sales.append(sales_amount)

    return months, sales

if __name__ == "__main__":
    months, sales = get_input_data()
    create_line_plot(months, sales)

