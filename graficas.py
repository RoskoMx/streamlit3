#Importamos los módulos
import pandas as pd
import streamlit as st
from PIL import Image

#Encabezado
st.header('Gráficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Grand Prix de Países Bajos")

#Imagen tal cuál está nombrada en el repositorio
image = Image.open('Verstappen-pole-lap-Zandvoort-Netherlands-2021.jpg')
st.image(image, caption='Max Verstappen')
#Descripción de la imagen

#Usuario
st.text_input("¿Cuál es tu nombre?", key="name")
st.session_state.name

#Como un print y no es necesario escribir st.text
st.text('¡Hola '+st.session_state.name+' !') 
'Hola cómo estás? ',st.session_state.name

#Generamos el Dataframe como si estuvieramos en Pandas
df = pd.read_csv('https://raw.githubusercontent.com/LilianaC/streamlit3/main/Datos%20F1%20Dutch%20GP%20-%20Sheet1.csv')
#Estos Dataframes se copian y pegan con la opción de raw, se pega la dirección de arriba del navegador
#Sí el checkbox es verdadero y solo escribimos df
if st.checkbox('Mostrar dataframe'):
    df

#Lista desplegable
option = st.selectbox(
    'Selecciona tu corredor favorito: ',
    #De dónde va a sacar la información
     df['DRIVER'])

'Tu selección: ', option

#Línea que muestra toda la info del renglón
df.loc[df['DRIVER'] == option]

#Gráfica
st.line_chart(
    df,
    x = 'AVG SPEED',
    y = 'LAP'
)
