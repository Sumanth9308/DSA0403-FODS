import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('house32.csv')
selected_feature = 'size'

plt.scatter(data[selected_feature], data['price'])
plt.title(f'Bivariate Analysis: {selected_feature} vs. Price')
plt.xlabel(selected_feature)
plt.ylabel('Price')
plt.show()

X = data[[selected_feature]]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')

plt.scatter(X_test, y_test, label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.title(f'Linear Regression: {selected_feature} vs. Price')
plt.xlabel(selected_feature)
plt.ylabel('Price')
plt.legend()
plt.show()
