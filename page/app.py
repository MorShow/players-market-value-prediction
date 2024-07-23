from flask import Flask, render_template, request, redirect, url_for, jsonify
import dill
import pandas as pd
import numpy as np

COLUMNS_COUNT = 45

NAMES_MAPPING = {
    'age': 'Age',
    'goals': 'Goals',
    'assists': 'Assists',
    'rank': 'Team_rank',
    'rating': 'Rating'
}

app = Flask(__name__)

with open(r"../final_model.pkl", 'rb') as file:
    av_model = dill.load(file)

@app.route('/', methods=['GET'])
def predict():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def enter():
    values_dictionary = request.values

    table = pd.read_csv("./online_data.csv")
    table = pd.concat([table, pd.DataFrame(np.zeros((1, COLUMNS_COUNT)), columns=table.columns[:COLUMNS_COUNT])])
    player_index = len(table.index) - 1

    for key, value in values_dictionary.items():
        key = NAMES_MAPPING.get(key)
        table.loc[player_index, key] = value

    X_train = table.loc[player_index].values.reshape(1, -1)

    market_value = av_model.predict(X_train)[0]

    return render_template('index.html', prediction=market_value)

if __name__ == '__main__':
    app.run(debug=True)
