from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    hours = float(request.form["hours"])
    attendance = float(request.form["attendance"])
    marks = float(request.form["marks"])

    prediction = model.predict([[hours, attendance, marks]])[0]

    if marks >= 90:
        GRADE = 'A'
    elif marks >= 75:
        GRADE = 'B'
    elif marks >= 65:
        GRADE = 'C'
    else:
        GRADE = 'D'

    return render_template(
    "index.html",
    prediction=prediction,
    GRADE=GRADE
)


if __name__ == "__main__":
    app.run(debug=True)