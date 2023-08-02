import matplotlib.pyplot as plt

def create_bar_plot():
    months = input("Enter the months (comma-separated): ").split(',')
    sales = [float(s) for s in input("Enter the corresponding sales (comma-separated): ").split(',')]

    plt.figure(figsize=(8, 6))
    plt.bar(months, sales, color='b', label='Monthly Sales')
    
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data (Bar Plot)')
    plt.grid(True)
    plt.legend()
    plt.show()

create_bar_plot()
