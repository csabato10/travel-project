from flask import Flask, render_template, request

app: Flask = Flask(__name__)

user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/take_off', methods=["GET", "POST"])
def take_off():
    return render_template("take_off.html")

if __name__ == '__main__':
    app.run(debug=True)