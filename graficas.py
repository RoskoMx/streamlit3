import pandas as pd
import streamlit as st

st.title("Gráficas de Pandas")
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')

if st.checkbox('Show dataframe'):
    df



option = st.selectbox(
    'Selecciona tu corredor favorito: ',
     df['DRIVER'])

'Tu selección: ', option

df.loc[df['DRIVER'] == option]


st.line_chart(
    df,
    x = 'AVG SPEED',
    y = 'LAP'
)
