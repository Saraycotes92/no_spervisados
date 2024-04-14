import matplotlib.pyplot as plt

def plot_clusters(data, labels, centers):
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.title('Visualización de Clusters K-Means')
    plt.show()
