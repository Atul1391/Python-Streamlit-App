import streamlit as st
import json
import requests

# Set title
st.title('Heart Attack Prediction Group 22')

# Sidebar
st.subheader('Predictors')

# Add sliders and select boxes for predictors
BMI = st.sidebar.slider('BMI', min_value=10, max_value=50, step=1)
PhysicalHealthDays = st.sidebar.slider('Physical Health Days', min_value=0, max_value=30, step=1)
MentalHealthDays = st.sidebar.slider('Mental Health Days', min_value=0, max_value=30, step=1)
SleepHours = st.sidebar.slider('Sleep Hours', min_value=0, max_value=24, step=1)
Sex_Male = st.sidebar.selectbox('Sex (Male)', [0, 1])
GeneralHealth_Poor = st.sidebar.selectbox('General Health (Poor)', [0, 1])
HadCOPD_Yes = st.sidebar.selectbox('Had COPD (Yes)', [0, 1])

# Create a dictionary of predictor values
predictors_dict = {
    'BMI': BMI,
    'PhysicalHealthDays': PhysicalHealthDays,
    'MentalHealthDays': MentalHealthDays,
    'SleepHours': SleepHours,
    'Sex_Male': Sex_Male,
    'GeneralHealth_Poor': GeneralHealth_Poor,
    'HadCOPD_Yes': HadCOPD_Yes
}

# Prediction button
if st.button('Predict'):
    try:
        # Send request to the model API
        response = requests.post(
            url="http://138.197.75.51:5001/invocations",
            json={'dataframe_records': [predictors_dict]},
        )

        # Check if the request was successful
        if response.ok:
            # Get prediction from response
            prediction = response.json().get('predictions')
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Failed to get prediction. Please try again later. {response.status_code} {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")
