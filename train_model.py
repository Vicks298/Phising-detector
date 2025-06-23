import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the dataset
data = pd.read_csv('phishing_dataset.csv')

# Split into features and labels
X = data.drop('result', axis=1)
y = data['result']

# Split data for training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as phishing_model.pkl")
