# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask,request, render_template

app=Flask(__name__,template_folder="templates")

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

count = 0

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
    model = pickle.load(open('demand_forecast.pkl', 'rb'))
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    print(features_value)
    
    features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine','city_code', 'region_code', 'category']
    prediction = model.predict(features_value)
    output=prediction[0]    
    return render_template("predict.html",prediction_text=int(output))

if __name__ == '__main__':
      app.run(debug=False)

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week



