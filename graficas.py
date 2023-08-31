import streamlit as st
st.title("Gráficas de Pandas")
st.header('Datos de la fórmula 1', divider='rainbow')

url = 'https://github.com/LilianaC/streamlit3/blob/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv'
df = pd.read_csv(url)

st.line_chart(
    df,
    x = 'DRIVER',
    y = 'AVG SPEED'
)
