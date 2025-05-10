import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample student data (you can replace this with actual student data)
data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'GPA': [3.2, 3.8, 2.9, 3.5, 3.0, 2.7, 3.9, 3.6, 3.1, 2.5],
    'study_hours': [15, 20, 10, 18, 14, 12, 25, 22, 16, 8],
    'attendance_rate': [90, 95, 85, 88, 92, 80, 98, 94, 90, 78]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 1: Feature Selection
features = df[['GPA', 'study_hours', 'attendance_rate']]

# Step 2: Scaling the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Step 3: Determine Optimal Number of Clusters (K) using Elbow Method
wcss = []  # List to store the WCSS values for each k
for i in range(2, 7):  # We will check from k=2 to k=6
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

# Plot the Elbow method graph
plt.plot(range(2, 7), wcss)
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.show()

# Based on the Elbow method, let's assume K=3 (as an example, you can adjust based on the plot)
optimal_k = 3

# Step 4: Apply K-Means Clustering
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Step 5: Visualization (Scatter plot of study_hours vs GPA)
plt.figure(figsize=(8, 6))
plt.scatter(df['study_hours'][df['Cluster'] == 0], df['GPA'][df['Cluster'] == 0], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(df['study_hours'][df['Cluster'] == 1], df['GPA'][df['Cluster'] == 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(df['study_hours'][df['Cluster'] == 2], df['GPA'][df['Cluster'] == 2], s = 100, c = 'red', label = 'Cluster 3')
plt.title('Clusters of Students (Study Hours vs GPA)')
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.legend()
plt.show()

# Step 6: Final dataset with student IDs and assigned clusters
print(df[['student_id', 'Cluster']])
