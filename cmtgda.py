import streamlit as st
import pandas as pd

# Título da página, divido em duas colunas, uma para a imagem
coluna_titulo, coluna_img = st.columns(2)
with coluna_titulo:
    st.title("Cmt Gda")
    
with coluna_img:
    st.image('logo11bia.png', width=80)
    
    
#upload do arquivo
df = pd.read_excel("previsao_cmt_gda.xlsx")

st.write("Escala de Comandante da Guarda")
st.dataframe(df)