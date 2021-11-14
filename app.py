import re
from flask import Flask, render_template, request

from helpers import budget_to_location

app: Flask = Flask(__name__)
desination: str = ""
user_number: int = 0


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/take_off', methods=["GET", "POST"])
def take_off():
    if request.method == "POST":
        global destination
        budget: str = request.form['budget']
        location: str = request.form['location']
        desination = budget_to_location(budget, location)
        return render_template(f"{desination}.html")
    return render_template("take_off.html")

@app.route('/beach', methods=["GET", "POST"])
def beach():
    if request.method == "POST":
        return render_template("beach.html")
    return render_template("beach.html")

@app.route('/city', methods=["GET", "POST"])
def city():
    if request.method == "POST":
        return render_template("city.html")
    return render_template("city.html")

@app.route('/wilderness', methods=["GET", "POST"])
def wilderness():
    if request.method == "POST":
        return render_template("wilderness.html")
    return render_template("wilderness.html")

@app.route('/wilmington', methods=["GET", "POST"])
def wilmington():
    if request.method == "POST":
        return render_template("wilmington.html")
    return render_template("wilmington.html")

@app.route('/miami', methods=["GET", "POST"])
def miami():
    if request.method == "POST":
        return render_template("miami.html")
    return render_template("miami.html")

@app.route('/cape_town', methods=["GET", "POST"])
def cape_town():
    if request.method == "POST":
        return render_template("cape_town.html")
    return render_template("cape_town.html")

@app.route('/charlotte', methods=["GET", "POST"])
def charlotte():
    if request.method == "POST":
        return render_template("charlotte.html")
    return render_template("charlotte.html")

@app.route('/new_york', methods=["GET", "POST"])
def new_york():
    if request.method == "POST":
        return render_template("new_york.html")
    return render_template("new_york.html")

@app.route('/dubai', methods=["GET", "POST"])
def dubai():
    if request.method == "POST":
        return render_template("dubai.html")
    return render_template("dubai.html")

@app.route('/boone', methods=["GET", "POST"])
def boone():
    if request.method == "POST":
        return render_template("boone.html")
    return render_template("boone.html")

@app.route('/yosemite', methods=["GET", "POST"])
def yosemite():
    if request.method == "POST":
        return render_template("yosemite.html")
    return render_template("yosemite.html")

@app.route('/ooty', methods=["GET", "POST"])
def ooty():
    if request.method == "POST":
        return render_template("ooty.html")
    return render_template("ooty.html")

@app.route('/', methods=["GET", "POST"])
def return_home():
    if request.method == "POST":
        return render_template("index.html")
    return render_template("index.html")

@app.route('/your_desination')
def final_desination():
    global desination
    return render_template(f"{desination}.html")

if __name__ == '__main__':
    app.run(debug=True)