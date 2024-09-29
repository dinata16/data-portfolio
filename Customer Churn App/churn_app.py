import streamlit as st
import joblib
import pandas as pd 
from PIL import Image

model = joblib.load('model_pipeline_full.pkl')

# Get the expected feature names from the model 
expected_features = model.feature_names_in_

def main():
    image = Image.open('churn.png')
    st.image(image, use_column_width=True)
    addselectbox = st.sidebar.selectbox("How would like to predict ?", ("Online", "Batch"))
    
    st.title("Customer Churn Prediction App")
    st.sidebar.info("This app is created to predict Customer Churn")
    
    if addselectbox == 'Online':
        state = st.text_input('State (Capital char)', max_chars=2)
        area_code = st.selectbox('Area code',['area_code_415', 'area_code_408','area_code_510'])
        account = st.number_input('Account length')
        international = st.selectbox('International plan',['Yes','No'])
        voicemail = st.selectbox('Voicemail plan',['Yes','No'])
        nvmail = st.number_input('Number vmail message')
        day_minutes = st.number_input('Total day minutes')
        day_charge = st.number_input('Total day charge')
        day_calls = st.number_input('Total day calls')
        eve_minutes = st.number_input('Total eve minutes')
        eve_calls = st.number_input('Total eve calls')
        eve_charge = st.number_input('Total eve charge')
        night_calls = st.number_input('Total night calls')
        night_minutes = st.number_input('Total night minutes')
        night_charge = st.number_input('Total night charge')
        intl_minutes = st.number_input('Total international minutes')
        intl_calls = st.number_input('Total international calls')
        intl_charge = st.number_input('Total international charge')
        cs_number = st.number_input('Number Customer Service Calls', max_value=9)

        output = ""
        output_prob = ""


        if st.button('Predict'):
            # Create a DataFrame from the input dictionary 
            input_df = pd.DataFrame({
              'state' : [state],
              'area_code':[area_code],
              'account_length':[account],
              'international_plan':[international],
              'voice_mail_plan':[voicemail],
              'number_vmail_messages':[nvmail],
              'total_day_minutes':[day_minutes],
              'total_day_charge':[day_charge],
              'total_day_calls':[day_calls],
              'total_eve_minutes':[eve_minutes],
              'total_eve_charge':[eve_charge],
              'total_eve_calls':[eve_calls],
              'total_night_minutes':[night_minutes],
              'total_night_charge':[night_charge],
              'total_night_calls':[night_calls],
              'total_intl_minutes':[intl_minutes],
              'total_intl_charge':[intl_charge],
              'total_intl_calls':[intl_calls],
              'number_customer_service_calls':[cs_number]
            })
            
            print("Expected features:", expected_features)
            print("Actual DataFrame columns:", input_df.columns)

            # Ensure the DataFrame has the same columns as expected by the model
            input_df = input_df[expected_features] 

            y_pred = model.predict_proba(input_df)[:, 1]  # Get probability of churn (class 1)
            churn = y_pred >= 0.5
            output_prob = float(y_pred[0])  
            output = bool(churn[0])  

            st.success(f"Churn: {output}, Risk rate: {round(output_prob*100, 4)} %")
    
    if addselectbox == 'Batch':
      uploaded_file = st.file_uploader("Upload csv file", type=['csv'])
      if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        predictions = model.predict(df)  
        #show sample data
        st.write("Sample Data: ")
        st.write(df.head(20))

        #sample prediction
        st.write("Sample Predictions: ")
        data_predict = pd.DataFrame({'id':df['id'], 'Churn':predictions})
        st.write(data_predict.head(20))


        # Option download
        st.download_button(
            label="Download Predictions",
            data=data_predict.to_csv(index=False),
            file_name='preditions_churn.csv',
            mime='text/csv',
        ) 
        



if __name__ == '__main__':
    main()