from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("cyboard"))

@app.route("/catering")
def catering():
    return render_template("catering.html")

@app.route("/cyboard")
def cyboard():
    return render_template("cyboard.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/patient")
def patient():
    return render_template("patient.html")


