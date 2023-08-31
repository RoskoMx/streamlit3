import streamlit as st
st.title("Gráficas de Pandas")
st.header('Datos de la fórmula 1', divider='rainbow')

df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')

st.line_chart(
    df,
    x = 'DRIVER',
    y = 'AVG SPEED'
)
