from flask import Flask
import pickle

app = Flask("app")
loaded_model = pickle.load(open('Model.pkl', 'rb'))

@app.route("/")
def home():
    return "Home Page"

@app.route("/prediction")
def predict():
    glucose = 150
    bmi = 25
    age = 40
    prediction = loaded_model.predict([[glucose, bmi, age]])[0]
    output = ""

    if prediction == 0:
        output = "Not Diabetic"
    else:
        output = "Diabetic"

    return "Prediction: " + output

if __name__ == '__main__':
    app.run(debug=True)