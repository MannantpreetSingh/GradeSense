from flask import Flask , render_template, request

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods =["POST"])
def predict():
   hours = request.form["hours"]
   attendance= request.form["attendance"]
   marks= request.form["marks"]
   
   return f" hours : {hours},attendance: {attendance}, marks {marks}"

if __name__ =="__main__":
    app.run(debug=True)
