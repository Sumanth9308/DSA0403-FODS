
import numpy as np

num_bedrooms = np.array([4, 2, 5, 3])
square_footage=np.array([2400, 2500, 3000, 1500])
sale_prices = np.array([250000, 250000, 300000, 350000])

prices_more_than_four_bedrooms = sale_prices[num_bedrooms > 4]

average_sale_price = np.mean(prices_more_than_four_bedrooms)

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
