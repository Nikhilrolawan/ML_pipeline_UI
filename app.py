import pickle
from streamlit_option_menu import option_menu
import streamlit as st
heart_model=pickle.load(open('model/model_pipeline.pkl','rb'))
with st.sidebar:
  selected=option_menu('Risk_Assesment',
                       ['Heart_Risk_Prediction'],
                       icons=['heart'],
                       default_index=0)
if(selected=='Heart_Risk_Prediction'):
  st.title('Heart Risk Prediction Using ML')
  age=st.text_input('Age')
  sex=st.text_input('sex type(male=1 or female=0)')
  cp=st.text_input('chest pain (yes=1 or no=0)')
  trestbps=st.text_input('Resting BP')
  chol=st.text_input('Serum cholestrol(mg/dl)')
  fbs=st.text_input('Fasting blood sugar>120(mg/dl)')
  restecg=st.text_input('resting ECG (values 0,1,2)')
  thalach=st.text_input('Max heart rate achieved')
  exang=st.text_input('Exercise induced angina')
  oldpeak=st.text_input(' ST depression induced by exercise relative to rest')
  slope=st.text_input('the slope of the peak exercise ST segment')
  ca=st.text_input('Calcium level')
  thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
  
  result=""
  if st.button('Test Heart Risk'):
    pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if pred[0]==1:
      result='The Person has HeartFailure Risk :('
    else:
      result='The Person does not have HeartFailure Risk :)'
  st.success(result)
