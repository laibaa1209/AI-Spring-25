import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.impute import SimpleImputer

# Step 1: Load the dataset
df = pd.read_csv("customers.csv")  # Columns: 'spending', 'age', 'visits', 'purchase_freq', 'category'

# Step 2: Clean the dataset
# Handle missing values with mean imputation for numerical columns
imputer = SimpleImputer(strategy='mean')
df[['spending', 'age', 'visits', 'purchase_freq']] = imputer.fit_transform(df[['spending', 'age', 'visits', 'purchase_freq']])

# Handle outliers - for simplicity, remove values greater than 3 standard deviations from the mean
for col in ['spending', 'age', 'visits', 'purchase_freq']:
    df = df[np.abs(df[col] - df[col].mean()) <= (3 * df[col].std())]

# Step 3: Feature scaling (standardize the features)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['spending', 'age', 'visits', 'purchase_freq']])

# Step 4: Prepare features and target variable
X = scaled_features
y = df['category']  # 'category' column contains high-value(1) or low-value(0)

# Step 5: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the model (Support Vector Machine for classification)
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Step 7: Make predictions and evaluate the model
y_pred = model.predict(X_test)

# Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Extract rules (from the coefficients of the linear SVM)
coefficients = model.coef_.flatten()
feature_names = ['spending', 'age', 'visits', 'purchase_freq']
rules = {feature_names[i]: coefficients[i] for i in range(len(coefficients))}
print("Rules (Feature importance):", rules)

# Step 9: Classify a new customer (e.g., with given features)
new_customer = {
    'spending': 1500,  # spending in the last 6 months
    'age': 30,
    'visits': 15,  # number of visits in the last 6 months
    'purchase_freq': 4  # purchases per month
}

new_customer_scaled = scaler.transform([[new_customer['spending'], new_customer['age'], new_customer['visits'], new_customer['purchase_freq']]])
prediction = model.predict(new_customer_scaled)
print("New customer classification:", "High-value" if prediction == 1 else "Low-value")
