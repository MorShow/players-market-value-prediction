from flask import Flask, render_template, request, redirect, url_for, jsonify
import dill
import pandas as pd
import numpy as np

COLUMNS_COUNT = 10

NAMES_MAPPING = {
    'age': 'Age',
    'goals': 'Goals',
    'assists': 'Assists',
    'rank': 'Team_rank',
    'rating': 'Rating',
    'mins': 'Mins',
    'ps': 'PS',
    'popularity': 'Popularity',
    'avgp': 'AvgP',
    'epl': 'From EPL'
}

COLUMNS_TO_MAP = ['rank', 'goals', 'assists', 'popularity', 'epl']

MAPPINGS = {
    'rank_a': 0,
    'rank_b': 1,
    'rank_c': 2,
    'goals_7': 0,
    'goals_14': 1,
    'goals_21': 2,
    'goals_28': 3,
    'assists_3': 0,
    'assists_7': 1,
    'assists_10': 2,
    'assists_14': 3,
    'popularity_1': 0,
    'popularity_2': 1,
    'popularity_3': 2,
    'popularity_4': 3,
    'popularity_5': 4,
    'epl_false': False,
    'epl_true': True
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
        if key in COLUMNS_TO_MAP:
            value = MAPPINGS.get(value)

        key = NAMES_MAPPING.get(key)
        table.loc[player_index, key] = value

    X_train = table.loc[player_index].values.reshape(1, -1)

    market_value = av_model.predict(X_train)[0]

    return render_template('index.html', prediction=market_value)

if __name__ == '__main__':
    app.run(debug=True)