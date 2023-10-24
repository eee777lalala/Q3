from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        mysalary=request.form['salary']
        mygender = request.form['gender']
        mymarital = request.form['marital']
        model = load('app/travel-recommender.joblib')
        np_arr = np.array([mysalary, mygender,mymarital])
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', href2='The suitable travel destination for you (salary:'+str(mysalary)+' ,gender:'+str(mygender)+',marital:'+str(mymarital)+') is:'+predictions_to_str)

