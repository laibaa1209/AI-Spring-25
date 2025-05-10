import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("house_data.csv")

# Step 2: Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)
df['neighborhood'].fillna(df['neighborhood'].mode()[0], inplace=True)

# Step 3: Encode categorical variables
le = LabelEncoder()
df['neighborhood_encoded'] = le.fit_transform(df['neighborhood'])

# Step 4: Feature selection
features = ['square_feet', 'bedrooms', 'bathrooms', 'age', 'neighborhood_encoded']
target = 'price'

# Visualize correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df[features + [target]].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation with Price")
plt.show()

# Step 5: Train/Test split
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model MSE: {mse:.2f}")
print(f"Model R² Score: {r2:.2f}")

# Step 8: Predict new house price
def predict_price(new_data):
    new_df = pd.DataFrame([new_data])
    new_df['neighborhood_encoded'] = le.transform([new_df['neighborhood'][0]])
    X_new = new_df[features]
    return model.predict(X_new)[0]

# Example prediction
new_house = {
    "square_feet": 2400,
    "bedrooms": 4,
    "bathrooms": 3,
    "age": 5,
    "neighborhood": "Greenwood"
}
predicted_price = predict_price(new_house)
print(f"Predicted house price: ${predicted_price:,.2f}")
