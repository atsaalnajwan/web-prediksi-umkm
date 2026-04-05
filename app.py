from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# --- 1. DATA DUMMY (Contoh Data Historis UMKM) ---
# Kita buat data sederhana agar model bisa belajar pola pertumbuhannya
# X = Tahun, y = Jumlah UMKM
X = np.array([[2020], [2021], [2022], [2023], [2024]])
y = np.array([1000, 1100, 1250, 1320, 1450])

# --- 2. TRAINING MODEL ---
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data tahun dari form (input user)
    tahun_input = request.form.get('tahun')
    
    if tahun_input:
        try:
            # Ubah input menjadi angka (float)
            tahun = float(tahun_input)
            
            # Lakukan prediksi menggunakan model yang sudah di-fit
            # Kita bungkus dalam [[ ]] karena model minta format 2D array
            prediksi = model.predict([[tahun]])
            
            # Ambil hasil prediksi dan bulatkan agar rapi
            hasil = round(prediksi[0], 2)
            
            return render_template('index.html', prediction_text=f"{hasil}")
        except Exception as e:
            return render_template('index.html', prediction_text="Error dalam perhitungan")
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)