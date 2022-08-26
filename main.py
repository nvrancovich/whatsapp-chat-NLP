import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from functions import parse_file

st.header('Whatsapp Chat Analytics')

st.write('Por Nicolás Vrancovich')

file = st.file_uploader('Agregá el archivo de tu chat acá', type='txt')

if file:
    parse_file(file)[:30]