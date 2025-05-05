from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
y = (y == 0).astype(int) # Convert to binary classification problem
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)
# Train SVM model with RBF kernel
svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(X_train, y_train)
# Make predictions
y_pred = svm.predict(X_test)
# Evaluate the model
print("SVM Accuracy:", accuracy_score(y_test, y_pred))