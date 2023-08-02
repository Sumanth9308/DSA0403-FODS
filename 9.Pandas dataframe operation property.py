import pandas as pd

data = {
    'PropertyID': [1, 2, 3, 4, 5],
    'Location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'Bedrooms': [3, 4, 5, 3, 6],
    'Area_SqFt': [1500, 1800, 2500, 2000, 3000],
    'Listing_Price': [200000, 250000, 350000, 280000, 450000]
}

property_data = pd.DataFrame(data)

location_input = input("Enter the location to get the average listing price: ")
bedrooms_input = int(input("Enter the minimum number of bedrooms to count properties: "))

location_avg_price = property_data[property_data['Location'] == location_input]['Listing_Price'].mean()
print(f"Average Listing Price of Properties in {location_input}: {location_avg_price}")

num_properties_with_more_bedrooms = len(property_data[property_data['Bedrooms'] > bedrooms_input])
print(f"Number of Properties with More than {bedrooms_input} Bedrooms: {num_properties_with_more_bedrooms}")

property_with_largest_area = property_data[property_data['Area_SqFt'] == property_data['Area_SqFt'].max()]
print("Property(ies) with the Largest Area:")
print(property_with_largest_area)
