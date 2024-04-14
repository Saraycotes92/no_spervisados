from data_loader import load_data
from kmeans_model import perform_kmeans
from plotting import plot_clusters

def main():
    # Carga de datos
    data = load_data('transport_data.csv')

    # Preparación de los datos para el clustering
    data_for_clustering = data[['Passengers', 'Time_of_Day']]  # Ajusta esto a tus variables

    # Ejecución del modelo K-Means
    labels, model = perform_kmeans(data_for_clustering, n_clusters=3)

    # Obtención de los centros de los clusters
    centers = model.cluster_centers_

    # Visualización de los clusters
    plot_clusters(data_for_clustering, labels, centers)

if __name__ == "__main__":
    main()
