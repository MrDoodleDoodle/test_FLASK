from flask import Flask, request, render_template, url_for, request, redirect


app = Flask(__name__)
app.secret_key = "justatest"


@app.route('/')
def index():
    return render_template("index.html")
