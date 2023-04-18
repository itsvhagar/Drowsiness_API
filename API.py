from flask import Flask,jsonify,request
import flask
from app import Drowsiness_Detection

app = Flask(__name__)
model = Drowsiness_Detection()

@app.route('/predict', methods = ["POST"])
def predict():
    file = request.data
    prediction = model.detect(file)
    if prediction:
        return jsonify(1)
    else:
        return jsonify(0)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
