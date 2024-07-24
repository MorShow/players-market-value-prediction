from flask import Flask, render_template, request, redirect, url_for, jsonify
from page_mappings import COLUMNS_TO_MAP, NAMES_MAPPING, MAPPINGS
import dill
import pandas as pd
import numpy as np

COLUMNS_COUNT = 10

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
    player_index = len(table.index)
    table = pd.concat([table, pd.DataFrame(np.zeros((1, COLUMNS_COUNT)), index=[player_index], columns=table.columns[:COLUMNS_COUNT])])

    for key, value in values_dictionary.items():
        if key in COLUMNS_TO_MAP:
            value = MAPPINGS.get(value)

        key = NAMES_MAPPING.get(key)
        table.loc[player_index, key] = value

    X_train = table.loc[player_index].values.reshape(1, -1)

    market_value = av_model.predict(X_train)[0]

    table.to_csv("./online_data.csv", index=False)

    return render_template('index.html', prediction='{:,}'.format(round(market_value))+'€')

if __name__ == '__main__':
    app.run(debug=True)