import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

def load_model(model_filename):
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    data = pd.read_csv('data.csv')

    feature_names = input("Enter the names of the features separated by spaces: ").split()
    target_variable = input("Enter the name of the target variable: ")

    X = data[feature_names]
    y = data[target_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_filename = 'model.pkl'
    model = load_model(model_filename)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Evaluation Metrics:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")

if __name__ == "__main__":
    main()
