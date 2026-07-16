from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    login = int(request.form["login"])

    failed = int(request.form["failed"])

    amount = float(request.form["amount"])

    device = int(request.form["device"])

    data = np.array([[login,failed,amount,device]])

    prediction = model.predict(data)

    if prediction[0] == -1:
        result = "⚠ Suspicious Transaction Detected"

    else:
        result = "✅ Normal Transaction"

    return render_template("index.html",prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
