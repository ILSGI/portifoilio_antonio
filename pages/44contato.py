import streamlit as st 
import gettext
_ = gettext.gettext


st.set_page_config(
    page_title="Lincoln - contato",
    page_icon="🏳️‍🌈"
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])
try:
  localizator = gettext.translation('base', localedir='locales', languages=[idioma])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.title("entre em contato por:")

st.subheader("📞: +55 (31) 984717322")
st.subheader("✉️: moreno1707@gmail.com")