import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
# from PIL import Image
model = pickle.load(open('Untitled2.sav', 'rb'))

st.title('Tesla Prediction')
st.sidebar.header('Tesla Data')
# FUNCTION
def user_report():
  # Date	 = st.sidebar.slider('Date', 50,100, 1 )
  Open	 = st.sidebar.slider('Open', 50,100, 1 )
  High	 = st.sidebar.slider('High', 0,100, 1 )
  Low = st.sidebar.slider('Low', 0,30, 1 )
  Close = st.sidebar.slider('Close', 0,10, 1 )
  AdjClose= st.sidebar.slider('Adj Close', 0,3, 1 )



  user_report_data = {
      # 'Date':Date,
      'Open':Open,
      'High':High,
      'Low':Low,
      'Close':Close,
      'Adj Close':AdjClose,
      # 'Volume':Volume
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Tesla Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Tesla Salary')
st.subheader('$'+str(np.round(salary[0], 2)))