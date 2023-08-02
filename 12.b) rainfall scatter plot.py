import matplotlib.pyplot as plt

def create_rainfall_scatter_plot(months, rainfall):
    plt.figure(figsize=(10, 6))
    plt.scatter(months, rainfall, marker='o', color='g', s=100)
    
    plt.title('Monthly Rainfall Data')
    plt.xlabel('Months')
    plt.ylabel('Rainfall (mm)')
    
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    
    print("Enter the monthly rainfall data:")
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    rainfall = []
    
    for month in months:
        rain = float(input(f"Enter rainfall for {month}: "))
        rainfall.append(rain)
    
    create_rainfall_scatter_plot(months, rainfall)
