from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression
from urllib.parse import parse_qs

app = Flask(__name__, template_folder="../templates")

# DATA
X = np.array([[2020], [2021], [2022], [2023], [2024]])
y = np.array([1000, 1100, 1250, 1320, 1450])

model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET"])
def index():
    hasil = None

    # 🔥 AMBIL QUERY SECARA MANUAL (WORK DI VERCEL)
    query = parse_qs(request.query_string.decode())

    if "tahun" in query:
        try:
            tahun = float(query["tahun"][0])
            prediksi = model.predict([[tahun]])
            hasil = round(prediksi[0], 2)
        except:
            hasil = "Error"

    return render_template("index.html", hasil=hasil)


# WAJIB UNTUK VERCEL
def handler(request):
    return app(request.environ, lambda status, headers: None)