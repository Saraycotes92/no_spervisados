import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    # Aquí podrías añadir cualquier preprocesamiento necesario, como limpieza o transformación de datos
    return data
