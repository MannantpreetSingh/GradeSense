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

    prediction = model.predict([[hours, attendance, marks]])
    score = (hours * 2) + (attendance * 0.5) + (marks * 1)
    if prediction[0]==1:
        result=  " pass" 
    else:
        result="fail "
    if score >= 150:
        GRADE = 'A'
    elif marks >= 100:
        GRADE = 'B'
    elif marks >= 65:
        GRADE = 'C'
    else:
        GRADE = 'D'

    return render_template(
    "index.html",
    prediction=result,
    GRADE=GRADE
)

if __name__ == "__main__":
    app.run()