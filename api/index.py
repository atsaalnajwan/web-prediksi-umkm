from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def home():
    return render_template("index.html")

# WAJIB untuk Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)