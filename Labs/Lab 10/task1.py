# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Importing the dataset
df = pd.read_csv('Mall_Customers.csv')
df.head()

# Extracting features for clustering (excluding 'customer_id')
x = df.drop(columns=['customer_id', 'Gender']).values  # assuming 'Gender' is categorical and not used for clustering

# Step 1: K-Means clustering without scaling
# Finding optimal number of clusters using the elbow method
wcss_list_no_scaling = []  # List to store WCSS values for the non-scaled data
for i in range(1, 11):
    kmeans_no_scaling = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans_no_scaling.fit(x)
    wcss_list_no_scaling.append(kmeans_no_scaling.inertia_)

plt.plot(range(1, 11), wcss_list_no_scaling)
plt.title('Elbow Method (Without Scaling)')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means clustering to the data without scaling (using 5 clusters from the elbow method)
kmeans_no_scaling = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict_no_scaling = kmeans_no_scaling.fit_predict(x)

# Visualizing the clusters without scaling
plt.scatter(x[y_predict_no_scaling == 0, 0], x[y_predict_no_scaling == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(x[y_predict_no_scaling == 1, 0], x[y_predict_no_scaling == 1, 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(x[y_predict_no_scaling == 2, 0], x[y_predict_no_scaling == 2, 1], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(x[y_predict_no_scaling == 3, 0], x[y_predict_no_scaling == 3, 1], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(x[y_predict_no_scaling == 4, 0], x[y_predict_no_scaling == 4, 1], s = 100, c = 'purple', label = 'Cluster 5')
plt.scatter(kmeans_no_scaling.cluster_centers_[:, 0], kmeans_no_scaling.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers (Without Scaling)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# Step 2: K-Means clustering with scaling applied to all features except 'age'
scaler = StandardScaler()
x_scaled = scaler.fit_transform(df.drop(columns=['customer_id', 'Gender', 'Age']))  # exclude 'age' from scaling

# Re-add 'age' column to the scaled data to avoid distorting its effect
x_scaled = np.column_stack((df['Age'], x_scaled))

# Finding optimal number of clusters using elbow method (with scaling)
wcss_list_scaled = []
for i in range(1, 11):
    kmeans_scaled = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans_scaled.fit(x_scaled)
    wcss_list_scaled.append(kmeans_scaled.inertia_)

plt.plot(range(1, 11), wcss_list_scaled)
plt.title('Elbow Method (With Scaling)')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means clustering with scaling (using 5 clusters from the elbow method)
kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict_scaled = kmeans_scaled.fit_predict(x_scaled)

# Visualizing the clusters with scaling
plt.scatter(x_scaled[y_predict_scaled == 0, 0], x_scaled[y_predict_scaled == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(x_scaled[y_predict_scaled == 1, 0], x_scaled[y_predict_scaled == 1, 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(x_scaled[y_predict_scaled == 2, 0], x_scaled[y_predict_scaled == 2, 1], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(x_scaled[y_predict_scaled == 3, 0], x_scaled[y_predict_scaled == 3, 1], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(x_scaled[y_predict_scaled == 4, 0], x_scaled[y_predict_scaled == 4, 1], s = 100, c = 'purple', label = 'Cluster 5')
plt.scatter(kmeans_scaled.cluster_centers_[:, 0], kmeans_scaled.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers (With Scaling)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
