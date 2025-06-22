import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

Gender = st.selectbox("Select your Gender", ["Male", "Female"])
Gender = 1 if Gender == "Male" else 0

Married = st.selectbox("Are you married" , ["Yes", "No"])
Married = 1 if Married=="Yes" else 0

Dependents = st.number_input("Enter your Dependents", step=1)

Education = st.selectbox("Select your education", ['Graduate', 'Not Graduate'])
Education = 1 if Education=="Graduate" else 0

Self_Employed = st.selectbox("Are you self employed", ["Yes", "No"])
Self_Employed = 1 if Self_Employed=="Yes" else 0

ApplicantIncome = st.number_input("Applicant Income")

CoapplicantIncom = st.number_input("Coapplicant Income")

LoanAmount = st.number_input("Loan Amount")

Loan_Amount_Term = st.number_input("Loan Amount Term in days")

Credit_History = st.selectbox("Credit History", ["Yes", "No"])
Credit_History = 1 if Credit_History=="Yes" else 0

Property_Area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

Property_Area = 2 if Property_Area == "Urban" else 1 if Property_Area == "Semiurban" else 0


if st.button("Predict"):
    query = np.array([Gender, Married,Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncom,LoanAmount, Loan_Amount_Term, Credit_History  ,Property_Area ])
    query = query.reshape(1,11)

    prediction = model.predict(query)

    if prediction[0] == 1:
        st.success("The person can get loan")
    else:
        st.error("The person cannot get loan")


