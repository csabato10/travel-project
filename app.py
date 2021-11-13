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

@app.route('/your_desination')
def final_desination():
    global desination
    return render_template(f"{desination}.html")

if __name__ == '__main__':
    app.run(debug=True)