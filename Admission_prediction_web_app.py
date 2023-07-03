import numpy as np
import pickle
import streamlit as st
import os

#loading the saved model

loaded_model=pickle.load(open("C:/Users/kakul/OneDrive/Desktop/streamlit/Admission task 1/Admission_model.sav",'rb'))

img = '''
<style>
.stApp {
    background-image: url("C:/Users/kakul/OneDrive/Desktop/streamlit/Admission task 1/ADMISSIONS FOR GRADUATION (1).png");
    background-size: cover;
    background-position: top center;
    background-repeat: no-repeat;
    background-attachment: local;
    background-blur;
    opacity: 1;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)

#creating a function for prediction

def Admission_prediction(input_data):
    
    #changing the input data to numpy array
    input_data_as_numpy_array=np.array(input_data,dtype=float)
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==1):
        return "The person has higher chance of getting graduation admission"
    else:
        return "The person has little or no chance of getting graduation admission"
    
def main():

    

    #giving title
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Graduation Admission Prediction Web App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

    #getting the input data from the user
    #GRE Score,TOEFL Score,University Rating,SOP,LOR ,CGPA,Research
   

    GRE_Score=st.text_input("Enter the GRE Score Obtained (Out of 340)")

    TOEFL_Score=st.text_input("Enter the TOEFL Score Obtained (Out of 120)")

    University_Rating=st.text_input("Enter the University Rating (Out of 5)")

    SOP=st.text_input("Enter the Statement of purpose Strength value (Out of 5)")

    LOR=st.text_input("Enter the Letter of REcommendation Strength value (Out of 5)")

    CGPA=st.text_input("Enter the Undergraduater CGPA  Obtained (Out of 10)")

    Research=st.text_input("Enter the Research Experience(Either 0 or 1)")

    #code for prediction

    Report=''

    #creating button for prediction

    if st.button("Graduation Admission Predicted Result"):

        Report=Admission_prediction([GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research])
    
    st.success(Report)




if __name__ =='__main__':
    main()
    

#python -m streamlit run "C:/Users/kakul/OneDrive/Desktop/streamlit/Admission task 1/Admission_prediction_web_app.py"  