# import dill
# import cloudpickle
import joblib
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd


# initialize app
app = Flask(__name__)


# # # load the model
# reg_model = cloudpickle.load(open("./regmodel.pkl", "rb"))
# scaler = cloudpickle.load(open("./scaler.pkl", "rb"))


# # load the model
scaler = joblib.load(open("./scaler.pkl", "rb"))
reg_model = joblib.load(open("./regmodel.pkl", "rb"))

# load the model
# reg_model = dill.load(open("./regmodel", "rb"))
# scaler = dill.load(open("./scaler", "rb"))



# home route
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict_api", methods = ["POST"])
def predict_api():
    # get data from POST request
    data = request.get_json()
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = reg_model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=9696)

