import streamlit as st
st.title("Gráficas de Pandas")
st.header('Datos de la fórmula 1', divider='rainbow')

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR6bzuHw55qEEuHYUyYTTxxV7xUcjrPuV5xG2mNyV_WNKX7M1Vq1aLRSiOZHV-M9UoNt7FJ_GfmzhBk/pub?gid=0&single=true&output=csv'
df = pd.read_csv(url)
len(df)

st.line_chart(
    df,
    x = 'DRIVER',
    y = 'AVG SPEED'
)
