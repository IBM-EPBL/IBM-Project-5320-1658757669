import pandas as pd
import numpy as np
import pickle
import os
import requests

API_KEY = "v3n6gq55C00788iHyYsU0cm1GG__LDIaxvhoZT6hB79m"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

from flask import Flask,request, render_template
app=Flask(__name__,template_folder="templates")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index')
def about():
    return render_template('index.html')
@app.route('/index1')
def page():
    return render_template('predict.html',prediction_text=0)
@app.route('/predict', methods=['GET', 'POST'])    
def predict():
    print("[INFO] loading model...")
    input_features = [float(x) for x in request.form.values()]
    print(input_features)
    features_value = [[np.array(input_features)]]
    print(features_value)

    payload_scoring = {"input_data":[{"field": [['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine','city_code', 'region_code', 'category']],"values": [input_features]}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/fd67c29a-39e2-4562-9a20-0ab40f1d0d8a/predictions?version=2022-11-30', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    prediction =response_scoring.json()
    print("dir(predict) :" ,dir(prediction))
    print(prediction)
    #print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])
    output = prediction['predictions'][0]['values'][0][0]

    return render_template("predict.html", prediction_text=int(output))

if __name__ == '__main__':
      app.run(debug=False)