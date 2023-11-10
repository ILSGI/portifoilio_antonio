import streamlit as st 
import gettext
_ = gettext.gettext

st.set_page_config(
    page_title="Antonio - competencias",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])
try:
  localizator = gettext.translation('base', localedir='locales', languages=[idioma])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.title("minhas competencias")

with st.expander("gestão de trafego"):
    "por diversos projetos e estudos, me tornei muito capaz e eficiente na gestão de trafego de um empresa, esse gráfico representa o crescimento de uma empresa após começar a trabalhar comigo"

    
with st.expander("gestão de midias sociais"):
    "justo a gestão de trafego, consegui gerar uma boa visão da marca atraindo respeito e credibilidade por meio das redes sociais, esse gráfico representa o número de seguidores de uma empresa após começar a trabalhar comigo:"
    
with st.expander("ingles"):
    "fernanda"
    
with st.expander("espanhol"):
    "rluciana"
    
    
