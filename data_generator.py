import pandas as pd
import numpy as np

def generate_data(n_samples=100):
    np.random.seed(0)
    station_id = np.random.randint(1, 10, size=n_samples)
    passengers = np.random.poisson(lam=200, size=n_samples)
    time_of_day = np.random.randint(1, 24, size=n_samples)

    data = pd.DataFrame({
        'Station_ID': station_id,
        'Passengers': passengers,
        'Time_of_Day': time_of_day
    })

    return data

def save_data(data, filepath='transport_data.csv'):
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    data = generate_data()
    save_data(data)
