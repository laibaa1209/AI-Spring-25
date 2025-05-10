import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Step 1: Prepare the data (exclude 'vehicle_type' from clustering)
X = df.drop(columns=['vehicle_serial_no', 'vehicle_type'])

# Step 2: K-Means clustering without scaling
# Using the elbow method to find the optimal number of clusters
wcss_no_scaling = []  # List for storing WCSS values
for i in range(1, 11):
    kmeans_no_scaling = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans_no_scaling.fit(X)
    wcss_no_scaling.append(kmeans_no_scaling.inertia_)

# Plotting the elbow method result for no scaling
plt.plot(range(1, 11), wcss_no_scaling)
plt.title('Elbow Method (Without Scaling)')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means clustering (choosing 4 clusters from the elbow method)
kmeans_no_scaling = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_predict_no_scaling = kmeans_no_scaling.fit_predict(X)

# Visualizing the clusters without scaling
plt.scatter(X.iloc[:, 0][y_predict_no_scaling == 0], X.iloc[:, 1][y_predict_no_scaling == 0], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(X.iloc[:, 0][y_predict_no_scaling == 1], X.iloc[:, 1][y_predict_no_scaling == 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(X.iloc[:, 0][y_predict_no_scaling == 2], X.iloc[:, 1][y_predict_no_scaling == 2], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(X.iloc[:, 0][y_predict_no_scaling == 3], X.iloc[:, 1][y_predict_no_scaling == 3], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(kmeans_no_scaling.cluster_centers_[:, 0], kmeans_no_scaling.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of vehicles (Without Scaling)')
plt.xlabel('Mileage')
plt.ylabel('Fuel Efficiency')
plt.legend()
plt.show()

# Step 3: K-Means clustering with scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scaling all features

# Elbow method for scaled data
wcss_scaled = []
for i in range(1, 11):
    kmeans_scaled = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans_scaled.fit(X_scaled)
    wcss_scaled.append(kmeans_scaled.inertia_)

# Plotting the elbow method result for scaled data
plt.plot(range(1, 11), wcss_scaled)
plt.title('Elbow Method (With Scaling)')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means clustering with scaling (choosing 4 clusters from the elbow method)
kmeans_scaled = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_predict_scaled = kmeans_scaled.fit_predict(X_scaled)

# Visualizing the clusters with scaling
plt.scatter(X_scaled[:, 0][y_predict_scaled == 0], X_scaled[:, 1][y_predict_scaled == 0], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(X_scaled[:, 0][y_predict_scaled == 1], X_scaled[:, 1][y_predict_scaled == 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(X_scaled[:, 0][y_predict_scaled == 2], X_scaled[:, 1][y_predict_scaled == 2], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(X_scaled[:, 0][y_predict_scaled == 3], X_scaled[:, 1][y_predict_scaled == 3], s = 100, c = 'black', label = 'Cluster 4')
plt.scatter(kmeans_scaled.cluster_centers_[:, 0], kmeans_scaled.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of vehicles (With Scaling)')
plt.xlabel('Mileage (scaled)')
plt.ylabel('Fuel Efficiency (scaled)')
plt.legend()
plt.show()
