import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/DELL/Desktop/Final SL/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/DELL/Desktop/Final SL/heart_model.sav', 'rb'))
ckd_model = pickle.load(open('C:/Users/DELL/Desktop/Final SL/ckd_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Kidney Disease Prediction'],
                           
                          icons=['activity','heart', 'circle'],
                          default_index=0)
    
    
# Diabetese Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    with st.form(key='Diabetes_prediction_form'):
        # get user input
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=15)
            SkinThickness = st.number_input('SkinThickness', min_value=0, max_value=65)

        with col2:
            Glucose = st.number_input('Glucose level', min_value=0, max_value=350)
            Insulin = st.number_input('Insulin', min_value=0, max_value=1917)
         

        with col3:
            Bloodpressure = st.number_input('Bloodpressure', min_value=0, max_value=180)
            BMI = st.number_input('BMI', min_value=0.00, max_value=70.00)

        col4, col5, col6 = st.columns(3)
        with col4:
            DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.000, max_value=3.000) 
        with col5:
            age = st.number_input('Age', min_value=1, max_value=120)
            


        # make prediction
        if st.form_submit_button('Predict Diabetes'):
            
            # create input array
            input_data = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, age]
            # make prediction using model
            prediction = diabetes_model.predict([input_data])[0]
            # show result
            if prediction == 1:
                st.success('The person is likely to have Diabetes.')
            else:
                st.success('The person is unlikely to have Diabetes.')

            # Create a DataFrame with user input and prediction
            df = pd.DataFrame({'Feature': ['Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age'],
                               'Value': [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, age]})
            
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    with st.form(key='heart_disease_prediction_form'):
        # get user input
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=1, max_value=120)
            trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300)

        with col2:
            sex = st.selectbox('Sex', options=['Male', 'Female'])
            chol = st.number_input('Serum Cholestoral in mg/dl', value=0, step=1)
         

        with col3:
            cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])

            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])

        col4, col5, col6 = st.columns(3)
        with col4:
            restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
            oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.00, max_value=8.00)
            

        with col5:
            thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250)
            slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2])
           

        with col6:
            exang = st.selectbox('Exercise Induced Angina', options=[0, 1])
            ca = st.number_input('Major Vessels Colored by Flourosopy', min_value=0, max_value=3  )

            thal = st.selectbox('Thal', options=[0, 1, 2, 3])

        # make prediction
        if st.form_submit_button('Predict Heart Disease'):
            # convert sex to integer
            if sex == 'Male':
                sex = 1
            else:
                sex = 0
            # create input array
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            # make prediction using model
            prediction = heart_disease_model.predict([input_data])[0]
            # show result
            if prediction == 1:
                st.success('The person is likely to have heart disease.')
            else:
                st.success('The person is unlikely to have heart disease.')

            # Create a DataFrame with user input and prediction
            df = pd.DataFrame({'Feature': ['Age', 'Sex', 'Chest Pain Type', 'Resting Blood Pressure', 'Serum Cholestoral', 'Fasting Blood Sugar', 
                                           'Resting Electrocardiographic Results', 'Maximum Heart Rate Achieved', 'Exercise Induced Angina', 
                                           'ST Depression Induced by Exercise', 'Slope of the Peak Exercise ST Segment', 
                                           'Major Vessels Colored by Flourosopy', 'Thal'],
                               'Value': [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]})

# Kidney Disease Prediction Page
if selected == 'Kidney Disease Prediction':

    # page title
    st.title('Kidney Disease Prediction using ML')

    with st.form(key='kidney_disease_prediction_form'):
        # get user input
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=1, max_value=120)
            bp = st.number_input('Blood Pressure', min_value=40, max_value=250)

        with col2:
            sg = st.number_input('Specific Gravity', min_value=0.0, max_value=2.0)
            al = st.number_input('Albumin', min_value=0, max_value=5)

        with col3:
            su = st.number_input('Sugar', min_value=0, max_value=5)
            rbc = st.selectbox('Red Blood Cells', options=['normal', 'abnormal'])

        col4, col5, col6 = st.columns(3)
        with col4:
            pc = st.selectbox('Pus Cell', options=['normal', 'abnormal'])
            pcc = st.selectbox('Pus Cell Clumps', options=['present', 'notpresent'])

        with col5:
            ba = st.selectbox('Bacteria', options=['present', 'notpresent'])
            bgr = st.number_input('Blood Glucose Random', min_value=0, max_value=500)

        with col6:
            bu = st.number_input('Blood Urea', min_value=0, max_value=400)
            sc = st.number_input('Serum Creatinine', min_value=0.0, max_value=15.0)

        col7, col8, col9 = st.columns(3)
        with col7:
            sod = st.number_input('Sodium', min_value=0, max_value=200)
            pot = st.number_input('Potassium', min_value=0, max_value=20)

        with col8:
            hemo = st.number_input('Hemoglobin', min_value=0.0, max_value=20.0)
            pcv = st.number_input('Packed Cell Volume', min_value=0, max_value=100)

        with col9:
            wc = st.number_input('White Blood Cell Count', min_value=0, max_value=25000)
            rc = st.number_input('Red Blood Cell Count', min_value=0, max_value=50)

        with st.expander('Other Features'):
            htn = st.selectbox('Hypertension', options=['yes', 'no'])
            dm = st.selectbox('Diabetes Mellitus', options=['yes', 'no'])
            cad = st.selectbox('Coronary Artery Disease', options=['yes', 'no'])
            appet = st.selectbox('Appetite', options=['good', 'poor'])
            pe = st.selectbox('Pedal Edema', options=['yes', 'no'])
            ane = st.selectbox('Anemia', options=['yes', 'no'])

        # make prediction
        if st.form_submit_button('Predict Kidney Disease'):
            # convert categorical features to binary
            rbc_binary = 1 if rbc == 'abnormal' else 0
            pc_binary = 1 if pc == 'abnormal' else 0
            pcc_binary = 1 if pcc == 'present' else 0
            ba_binary = 1 if ba == 'present' else 0
            htn_binary = 1 if htn == 'yes' else 0
            dm_binary = 1 if dm == 'yes' else 0
            cad_binary = 1 if cad == 'yes' else 0
            appet_binary = 1 if appet == 'good' else 0
            pe_binary = 1 if pe == 'yes' else 0
            ane_binary = 1 if ane == 'yes' else 0

            # create input array
            input_data = [age, bp, sg, al, su, rbc_binary, pc_binary, pcc_binary, ba_binary, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn_binary, dm_binary, cad_binary, appet_binary, pe_binary, ane_binary]
            # make prediction using model
            prediction = ckd_model.predict([input_data])[0]
            # show result
            if prediction == 1:
                st.success('The person is likely to have kidney disease.')
            else:
                st.success('The person is unlikely to have kidney disease.')

            # Create a DataFrame with user input and prediction
            df = pd.DataFrame({'Feature': ['Age', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar', 'Red Blood Cells', 'Pus Cell', 'Pus Cell Clumps', 'Bacteria', 
                                           'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 
                                           'Red Blood Cell Count', 'Hypertension', 'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia'],
                               'Value': [age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]})

# Download button for user input and prediction
if 'df' in locals():
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Prediction Data",
        data=csv,
        file_name='prediction_data.csv',
        mime='text/csv'
    )
