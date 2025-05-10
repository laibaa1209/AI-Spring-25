import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
df = pd.read_csv("emails.csv")  # Assumed columns: 'content', 'sender', 'has_link', 'label'

# Step 2: Basic preprocessing
df['email_length'] = df['content'].apply(len)

# Encode sender
le = LabelEncoder()
df['sender_encoded'] = le.fit_transform(df['sender'])

# Binary encode hyperlinks
df['has_link'] = df['has_link'].astype(int)

# Step 3: Vectorize text (TF-IDF)
tfidf = TfidfVectorizer(stop_words='english', max_features=300)
X_tfidf = tfidf.fit_transform(df['content'])

# Combine features
X_additional = df[['email_length', 'has_link', 'sender_encoded']].reset_index(drop=True)
from scipy.sparse import hstack
X = hstack([X_tfidf, X_additional])
y = df['label']

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Deploy - Classify new email
def classify_email(content, sender, has_link):
    email_len = len(content)
    sender_encoded = le.transform([sender])[0] if sender in le.classes_ else 0
    tfidf_vec = tfidf.transform([content])
    add_features = np.array([[email_len, int(has_link), sender_encoded]])
    final_input = hstack([tfidf_vec, add_features])
    return model.predict(final_input)[0]

# Example prediction
new_email = {
    "content": "You've won a free iPhone! Click this link to claim your prize.",
    "sender": "promo@fakesite.com",
    "has_link": True
}
result = classify_email(**new_email)
print("Spam" if result == 1 else "Not Spam")
