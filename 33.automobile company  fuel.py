import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

data = pd.read_csv('car33.csv')

selected_features = ['engine_size', 'horsepower', 'fuel_efficiency']  # Choose relevant features
target_feature = 'price'

X = data[selected_features]
y = data[target_feature]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error:", mae)

coefficients = model.coef_
feature_importance = pd.Series(coefficients, index=selected_features).sort_values(ascending=False)

print("Feature Importance:")
print(feature_importance)
