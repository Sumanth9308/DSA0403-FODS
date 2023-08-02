import matplotlib.pyplot as plt

def create_line_plot():
    months = input("Enter the months (comma-separated): ").split(',')
    sales = [float(s) for s in input("Enter the corresponding sales (comma-separated): ").split(',')]

    plt.figure(figsize=(8, 6))  
    plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
    
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data (Line Plot)')
    plt.grid(True)
    plt.legend()
    plt.show()

create_line_plot()
