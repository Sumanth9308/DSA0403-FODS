import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

data = pd.read_csv('medicalcsv34.csv')  

label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['treatment_outcome'] = label_encoder.fit_transform(data['treatment_outcome'])

data = pd.get_dummies(data, columns=['blood_pressure', 'cholesterol'], drop_first=True)

X = data.drop('treatment_outcome', axis=1)
y = data['treatment_outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_test_original = label_encoder.inverse_transform(y_test)
y_pred_original = label_encoder.inverse_transform(y_pred)

accuracy = accuracy_score(y_test_original, y_pred_original)
precision = precision_score(y_test_original, y_pred_original, pos_label='Good')
recall = recall_score(y_test_original, y_pred_original, pos_label='Good')
f1 = f1_score(y_test_original, y_pred_original, pos_label='Good')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

print("Classification Report:\n", classification_report(y_test_original, y_pred_original))
