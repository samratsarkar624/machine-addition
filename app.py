from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    actual = None
    number1 = None
    number2 = None

    if request.method == "POST":

        number1 = float(request.form["number1"])
        number2 = float(request.form["number2"])

        prediction = round(predict(number1, number2), 2)

        actual = number1 + number2

    return render_template(
        "index.html",
        prediction=prediction,
        actual=actual,
        number1=number1,
        number2=number2
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)