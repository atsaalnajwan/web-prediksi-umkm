from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# --- DATA DUMMY ---
X = np.array([[2020], [2021], [2022], [2023], [2024]])
y = np.array([1000, 1100, 1250, 1320, 1450])

# --- TRAIN MODEL ---
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None

    if request.method == 'POST':
        tahun_input = request.form.get('tahun')

        if tahun_input:
            try:
                tahun = float(tahun_input)
                prediksi = model.predict([[tahun]])
                hasil = round(prediksi[0], 2)
            except:
                hasil = "Terjadi kesalahan"

    return render_template('index.html', hasil=hasil)


if __name__ == '__main__':
    app.run(debug=True)