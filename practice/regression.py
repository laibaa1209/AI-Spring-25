import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes  # Example dataset

# Load example dataset (you can replace this with your own)
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# ------------------- Train-Test Split -------------------
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(x_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(x_test)
print("Train-Test Split MSE:", mean_squared_error(y_test, y_pred))

# ------------------- K-Fold Cross Validation -------------------
print("\nK-Fold Cross Validation:")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
kf_mse = []

for train_idx, test_idx in kf.split(X):
    X_train_kf, X_test_kf = X.iloc[train_idx], X.iloc[test_idx]
    y_train_kf, y_test_kf = y[train_idx], y[test_idx]

    model_kf = LinearRegression()
    model_kf.fit(X_train_kf, y_train_kf)
    y_pred_kf = model_kf.predict(X_test_kf)

    mse = mean_squared_error(y_test_kf, y_pred_kf)
    kf_mse.append(mse)

print("K-Fold MSEs:", kf_mse)
print("Mean K-Fold MSE:", np.mean(kf_mse))

# ------------------- Leave-One-Out Cross Validation -------------------
print("\nLeave-One-Out Cross Validation:")
loo = LeaveOneOut()
loo_mse = []

for train_idx, test_idx in loo.split(X):
    X_train_loo, X_test_loo = X.iloc[train_idx], X.iloc[test_idx]
    y_train_loo, y_test_loo = y[train_idx], y[test_idx]

    model_loo = LinearRegression()
    model_loo.fit(X_train_loo, y_train_loo)
    y_pred_loo = model_loo.predict(X_test_loo)

    mse = mean_squared_error(y_test_loo, y_pred_loo)
    loo_mse.append(mse)

print("Mean LOOCV MSE:", np.mean(loo_mse))

#other method
df = pd.read_csv('your_dataset.csv')
X = df.drop('target_column', axis=1)
y = df['target_column']


#REG PLOT
# ---------- Regression Line (LOBEST) Plot using Seaborn ----------
plt.figure(figsize=(8, 5))
sns.regplot(x=x_test.iloc[:, 0], y=y_test, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Regression Line (LOBEST) on Test Data")
plt.xlabel(data.feature_names[0])
plt.ylabel("Target")
plt.grid(True)
plt.show()
