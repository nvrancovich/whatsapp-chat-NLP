import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from whatstk.whatsapp.objects import WhatsAppChat

st.header('Whatsapp Chat Analytics')

st.write('Por Nicolás Vrancovich')

file = st.file_uploader('Agregá el archivo de tu chat acá', type='txt')

if file:
    df = WhatsAppChat.from_source(file).df
    df[:30]