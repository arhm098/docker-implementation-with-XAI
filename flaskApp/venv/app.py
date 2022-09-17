from gettext import install
from json import load
from pydoc import render_doc
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import balanced_accuracy_score
from sklearn.naive_bayes import GaussianNB
from flask import Flask  			
# from opentelemetry import trace
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.sdk.resources import SERVICE_NAME, Resource
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor

# trace.set_tracer_provider(
# TracerProvider(
#         resource=Resource.create({SERVICE_NAME: "my-helloworld-service"})
#     )
# )
# tracer = trace.get_tracer(__name__)

# # create a JaegerExporter
# jaeger_exporter = JaegerExporter(
#     # configure agent
#     agent_host_name='localhost',
#     agent_port=6831,
#     # optional: configure also collector
#     collector_endpoint='http://localhost:14268/api/traces?format=jaeger.thrift',
#     # username=xxxx, # optional
#     # password=xxxx, # optional
#     # max_tag_value_length=None # optional
# )

# # Create a BatchSpanProcessor and add the exporter to it
# span_processor = BatchSpanProcessor(jaeger_exporter)

# add to the tracer
#trace.get_tracer_provider().add_span_processor(span_processor)
######################################################################
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.get_tracer(__name__)
app = Flask(__name__)



@app.route("/",methods = ['GET','POST'])
def index():
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
    loaded_model = joblib.load('loanPredictionModel.sav')
    
    if request.method == "POST":
        with tracer.start_as_current_span("getting user data") as parent:
            parent.add_event("POST")
            loan_amount = request.form.get("f_loan_amount")
            term = request.form.get("f_term")
            int_rate = request.form.get("f_int_rate")
            installment = request.form.get("f_installment")
            sub_grade = request.form.get("f_sub_grade")
            emp_length = request.form.get("f_emp_length")
            annual_inc = request.form.get("f_annual_inc")
            dti = '19'
            earliest_cr_line = '50'
            open_acc = request.form.get("f_open_acc")
            pub_rec = request.form.get("f_pub_rec") 
            revol_bal = request.form.get("f_revol_bal")
            revol_util = request.form.get("f_revol_util")
            total_acc = request.form.get("f_total_acc")
            mort_acc = request.form.get("f_mort_acc")
            pub_rec_bankruptcies = '0'
            weights = {'A':60,'B':50,'C':40,'D':30,'E':20,'F':10,'G':0}
            sub_grade = weights[str(sub_grade)]
            with tracer.start_as_current_span("processing DATA",attributes={'loan_amount':loan_amount,'term':term,'int_rate':int_rate,'installment':installment,'sub_grade':sub_grade,'emp_length':emp_length,'annual_inc':annual_inc,'dti':dti,'earliest_cr_line':earliest_cr_line,'open_acc':open_acc,'pub_rec':pub_rec,'revol_bal':revol_bal,'revol_util':revol_util,'total_acc':total_acc,'pub_rec_bankruptcies':pub_rec_bankruptcies,'mort_acc':mort_acc}) as child:
                child.add_event("model get DATA")
                data = np.array([[int(loan_amount),int(term),int(int_rate),int(installment),int(sub_grade),int(emp_length),int(annual_inc),int(dti),int(earliest_cr_line),int(open_acc),int(pub_rec),int(revol_bal),int(revol_util),int(total_acc),int(pub_rec_bankruptcies),int(mort_acc)]])
                pred = loaded_model.predict(data)
                trace.get_current_span()
            trace.get_current_span()
        with tracer.start_as_current_span("sending result to site",attributes={'result':str(pred[0])}):
            return render_template("result.html",result = str(pred[0]))
    return render_template("index.html");   

