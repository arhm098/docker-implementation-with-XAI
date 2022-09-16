from json import load
from pydoc import render_doc
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from flask import Flask  			
from opentelemetry import trace


tracer = trace.get_tracer(__name__)
app = Flask(__name__)




@app.route("/",methods = ['GET','POST'])
def index():
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
    loaded_model = joblib.load('finalized_model.sav')
    
    if request.method == "POST":
       with tracer.start_as_current_span("get DATA") as rollspan:
        sex = request.form.get("fsex")
        age = request.form.get("fage")
        cp = request.form.get("fcp")
        trestbps = request.form.get("ftrestbps")
        chol = request.form.get("fchol")
        data = np.array([[int(age),int(sex),int(cp),int(trestbps),int(chol),0,1,2,2,3]])
        pred = loaded_model.predict(data)
        return '<p>'+'atleast we here'+str(pred[0])+'<p>'
    return render_template("index.html");   

