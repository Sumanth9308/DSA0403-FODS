import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv('csv35.csv')

X = data[['TotalSpent', 'Frequency']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

optimal_k = 3

kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(X['TotalSpent'], X['Frequency'], c=data['Cluster'], cmap='rainbow')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=300, c='black', marker='X')
plt.title('Customer Segmentation')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.show()

for i in range(optimal_k):
    cluster_data = data[data['Cluster'] == i]
