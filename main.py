import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from functions import parse_file

st.header('Whatsapp Chat Analytics')

st.write('Por Nicolás Vrancovich')

file = st.file_uploader('Agregá el archivo de tu chat acá')

if file:
    dataframe = pd.read_csv(file)
    st.write(dataframe)