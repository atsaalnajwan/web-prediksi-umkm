import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Tahun": [2017, 2018, 2019, 2020],
    "Nilai": [873, 927, 985, 1046]
}

df = pd.DataFrame(data)

X = df[['Tahun']]
Y = df['Nilai']

# Training model
model = LinearRegression()
model.fit(X, Y)

# Fungsi prediksi
def prediksi(tahun):
    tahun = np.array([[tahun]])
    return model.predict(tahun)[0]