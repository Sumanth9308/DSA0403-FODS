import pandas as pd

def read_stock_data(filename):
    try:
        stock_data = pd.read_csv(filename)
        return stock_data
    except Exception as e:
        print("Error reading the CSV file:", e)
        return None

def calculate_stock_variability(stock_data):
    if stock_data is None:
        return None
    
    closing_prices = stock_data['ClosingPrice']
    mean_price = closing_prices.mean()
    price_std = closing_prices.std()
    return mean_price, price_std

def analyze_price_movements(mean_price, price_std):
    print("Insights into Stock Price Movements:")
    print("Mean Price: {:.2f}".format(mean_price))
    print("Price Standard Deviation: {:.2f}".format(price_std))
    
    if price_std > 0:
        print("The stock's price has shown variability.")
        if price_std < mean_price * 0.1:
            print("The variability is relatively low.")
        elif price_std < mean_price * 0.2:
            print("The variability is moderate.")
        else:
            print("The variability is relatively high.")
    else:
        print("There is not enough variability to analyze.")

def main():
    filename = 'csv36.csv'
    stock_data = read_stock_data(filename)
    
    if stock_data is not None:
        mean_price, price_std = calculate_stock_variability(stock_data)
        analyze_price_movements(mean_price, price_std)

if __name__ == "__main__":
    main()
