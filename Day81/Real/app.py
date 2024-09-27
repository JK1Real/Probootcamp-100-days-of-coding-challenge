from flask import Flask,render_template,request
import pandas as pd
import pickle
import re
import numpy as np

with open('model.pkl', 'rb') as file:
    linear_model=pickle.load(file=file)

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    data=""
    prediction=""
    columns=""
    if request.method=='GET':
        data=request.args.get('data')
        print(data)
        if data is not None:
            data = [float(i) for i in re.split(r'[%\t]', data)]
            columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT']
            datain_dataframe=pd.DataFrame(data=[data],columns=[columns])
            print(datain_dataframe)
            prediction=np.exp(linear_model.predict(datain_dataframe)[0])
        print(data)

    return render_template('index.html',prediction=prediction,data=data,columns=columns)

if "__main__"==__name__:
    app.run(debug=True)