# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd

df=pd.read_csv('claimants.csv')

st.line_chart(df['LOSS'])

st.title('Machine Learnig Model:coffee:')
st.title('Rainy Season Started!!!!:umbrella_with_rain_drops:')
st.markdown('This is my first Web Application! :wave:')
st.text('ML Model!')

st.selectbox('Select your city',('Pune','Mumbai','Delhi','Chennai','Hyderabad'))

st.number_input('Select your age:',min_value=10, max_value=60)