import numpy as np
import pickle
import streamlit as st

@st.cache_resource  #Avoids reloading the model on every prediction
def load_model():
    return pickle.load(open("diabetes_model.sav",'rb'))

laoded_model=load_model()

def predict_diabetes(input_data):
    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshaping the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    std_data=loaded_model.predict(input_data_reshaped)
    print(std_data)

    if (std_data[0]==0):
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
input_data=(5,166,72,19,175,25.8,0.587,51)
print(predict_diabetes(input_data))

def main():
    st.title("Diabetes Prediction Web App")

    Pregnancies=st.text_input("Number of Pregnancies")
    Glucose=st.text_input("Glucose Level")
    BloodPressure=st.text_input("Blood Pressure value")
    SkinThickness=st.text_input("Skin Thickness value")
    Insulin=st.text_input("Insulin Level")
    BMI=st.text_input("BMI value")
    DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
    Age=st.text_input("Age of the Person")

    diagnosis=""
    if st.button("Diabetes Test Result"):
        diagnosis=predict_diabetes((Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age))
    st.success(diagnosis)


if __name__=='__main__':
    main()