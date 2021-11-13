from flask import Flask, render_template, request

app: Flask = Flask(__name__)

user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)