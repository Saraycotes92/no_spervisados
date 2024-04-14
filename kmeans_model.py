from sklearn.cluster import KMeans

def perform_kmeans(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    return kmeans.labels_, kmeans
