from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np 
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_prediction


app = FastAPI(
    title="Loan Prediction API with jenkins",
    description="This is a Loan Prediction API",
    version="1.0.0",
)

origins =["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoanPrediction(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str



@app.get("/")
def index():
    return {"message": "Welcome to the loan prediction app using jenkins: Demo Version 1.5"}


@app.post("/predict_api")
def predict_loan_status(loan_details: LoanPrediction):
    data=loan_details.model_dump()
    predictions=generate_prediction([data])["Prediction"][0]
    if predictions == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"

    return {"status of loan application": pred}



@app.post("/prediction_ui")
def predict_gui ( Gender: str,
    Married: str,
    Dependents: str,
    Education: str,
    Self_Employed: str,
    ApplicantIncome: float,
    CoapplicantIncome: float,
    LoanAmount: float,
    Loan_Amount_Term: float,
    Credit_History: float,
    Property_Area: str
    ) :

    input_data = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]

    cols = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
    
    data_dict = dict(zip(cols,input_data))
    predictions = generate_prediction([data_dict])["Prediction"][0]

    if predictions == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"

    return {"status of loan application": pred}

if __name__ =="__main__":
    uvicorn.run(app, host ="0.0.0.0", port =8005)

