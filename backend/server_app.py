from flask import Flask, render_template, request, redirect, url_for, jsonify
import joblib
import pickle
import dill

app = Flask(__name__)

with open(r"../final_model.pkl", 'rb') as file:
    av_model = dill.load(file)

@app.route('/')
def predict():
    data = request.json
    prediction = av_model.predict(data)
    return jsonify(f'prediction: {prediction.tolist()}')

if __name__ == '__main__':
    app.run(debug=True)
