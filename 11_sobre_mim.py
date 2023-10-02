import streamlit as st 
import gettext
_ = gettext.gettext

st.set_page_config(
    page_title="Antonio - sobre mim",
    page_icon="🏳️‍🌈"
)
 
idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])
try:
  localizator = gettext.translation('base', localedir='locales', languages=[idioma])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.title("sobre mim")
st.write("Antonio de Souza Moreno")
st.write("olá meu nome Antonio, sou apaixonado pelo mundo digital e sou um jovem gestor de trefego nascido no ano de 2007, meu trabalho é transformar negocios por meio do mundo digital, posso ajuda-lo a crescer cada paixão por negocios e transforma-lo em um sucesso!")
