import matplotlib.pyplot as plt

def create_temperature_line_plot(months, temperatures):
    plt.figure(figsize=(10, 6))
    plt.plot(months, temperatures, marker='o', color='b', linestyle='-', linewidth=2)
    
    plt.title('Monthly Temperature Data')
    plt.xlabel('Months')
    plt.ylabel('Temperature (°C)')
    
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":

    print("Enter the monthly temperature data:")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    temperatures = []
    
    for month in months:
        temperature = float(input(f"Enter temperature for {month}: "))
        temperatures.append(temperature)
    
    create_temperature_line_plot(months, temperatures)
