
 

import streamlit as st

import plotly.express as px

 

 

st.set_page_config(

    layout="wide",

    page_title="Simple Dashboard"

)

df= px.data.tips()

 

# side bar

x= st.sidebar.checkbox('Show Data', True, key=1)

day= st.sidebar.selectbox('Select day', df['day'].unique())

time= st.sidebar.selectbox('Select Meal Time', df['time'].unique())

 

size= st.sidebar.radio("Select how many Dishes", sorted(df['size'].unique()), 3, horizontal=True)
