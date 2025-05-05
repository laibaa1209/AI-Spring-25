import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
# Load sample dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# ------------------- Train-Test Split -------------------
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
DT = DecisionTreeClassifier()
DT.fit(x_train, y_train)

# Predict
PredictionDT = DT.predict(x_test)

# ------------------- Metrics -------------------
print("Predictions:", PredictionDT)

# Accuracy
train_acc = DT.score(x_train, y_train)
test_acc = accuracy_score(y_test, PredictionDT)
print(f"\nTraining Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy: {test_acc * 100:.2f}%")

# Confusion Matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, PredictionDT)
print(cm)
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", xticklabels=data.target_names, yticklabels=data.target_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, PredictionDT, target_names=data.target_names))

# Individual Metrics (macro average)
precision = precision_score(y_test, PredictionDT, average='macro')
recall = recall_score(y_test, PredictionDT, average='macro')
f1 = f1_score(y_test, PredictionDT, average='macro')

print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"F1 Score: {f1 * 100:.2f}%")

# ------------------- K-Fold Cross Validation -------------------
print('\n==================== K-Fold Cross Validation ==================')
kf = KFold(n_splits=5, shuffle=True, random_state=42)
kf_scores = []

for train_index, test_index in kf.split(X):
    X_train_kf, X_test_kf = X.iloc[train_index], X.iloc[test_index]
    y_train_kf, y_test_kf = y[train_index], y[test_index]

    model_kf = DecisionTreeClassifier()
    model_kf.fit(X_train_kf, y_train_kf)
    preds_kf = model_kf.predict(X_test_kf)
    kf_scores.append(accuracy_score(y_test_kf, preds_kf))

print("K-Fold Accuracies:", [f"{score*100:.2f}%" for score in kf_scores])
print(f"Mean K-Fold Accuracy: {np.mean(kf_scores) * 100:.2f}%")

# ------------------- Leave-One-Out Cross Validation -------------------
print('\n==================== LOOCV ==================')
loo = LeaveOneOut()
loo_scores = []

for train_index, test_index in loo.split(X):
    X_train_loo, X_test_loo = X.iloc[train_index], X.iloc[test_index]
    y_train_loo, y_test_loo = y[train_index], y[test_index]

    model_loo = DecisionTreeClassifier()
    model_loo.fit(X_train_loo, y_train_loo)
    pred_loo = model_loo.predict(X_test_loo)
    loo_scores.append(accuracy_score(y_test_loo, pred_loo))

print(f"Mean LOOCV Accuracy: {np.mean(loo_scores) * 100:.2f}%")

#----------ROC CURVE-------
# Assuming the model has been trained and 'PredictionDT' holds class predictions
# To compute ROC, we need the probability estimates, not just the predicted class.
# For binary classification, use the probabilities of the positive class.
# Get probabilities for the positive class
probabilities = DT.predict_proba(x_test)[:, 1] # Get the probability for class
'1'
# Calculate ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, probabilities)
# Calculate ROC_AUC Score
roc_auc = roc_auc_score(y_test, probabilities)
# Plot ROC curve with shaded area under the curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC ={roc_auc:.2f})')
plt.fill_between(fpr, tpr, color='skyblue', alpha=0.4)
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve with AUC Area')
plt.legend(loc='lower right')
plt.show()