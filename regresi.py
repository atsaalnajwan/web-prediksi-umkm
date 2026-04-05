# 1. Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Dataset
data = {
    "Tahun": [2017, 2018, 2019, 2020],
    "Nilai": [873, 927, 985, 1046]
}

df = pd.DataFrame(data)

# 3. Menentukan variabel
X = df[['Tahun']]   # input
Y = df['Nilai']     # target

# 4. Membuat model
model = LinearRegression()
model.fit(X, Y)

# 5. Prediksi (contoh prediksi tahun 2021)
tahun_baru = np.array([[2021]])
prediksi_2021 = model.predict(tahun_baru)

# 6. Prediksi semua data (untuk grafik)
Y_pred = model.predict(X)

# 7. Evaluasi model
mae = mean_absolute_error(Y, Y_pred)
mse = mean_squared_error(Y, Y_pred)
r2 = r2_score(Y, Y_pred)

print("=== Evaluasi Model ===")
print("MAE :", mae)
print("MSE :", mse)
print("R2  :", r2)

print("\nPrediksi tahun 2021 =", prediksi_2021[0])

# 8. Visualisasi
plt.scatter(X, Y, color='blue', label="Data Aktual")
plt.plot(X, Y_pred, color='red', label="Garis Regresi")
plt.xlabel("Tahun")
plt.ylabel("Nilai")
plt.title("Regresi Linear Tahun vs Nilai")
plt.legend()
plt.show()