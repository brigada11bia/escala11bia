import streamlit as st
from openpyxl import load_workbook

st.set_page_config(
        page_title="Escalas de Serviço",
        page_icon="logo.ico"
    )


pagina = st.navigation(
    [st.Page("sobreaviso.py", title="Escala Sobreaviso"),
    st.Page("sgtdia.py", title="Escala de Sargento Dia"),
    st.Page("cmtgda.py", title="Escala de Cmt Gda")],
    position='sidebar')
pagina.run()

