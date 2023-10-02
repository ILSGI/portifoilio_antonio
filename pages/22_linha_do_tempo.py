import streamlit as st
from streamlit_timeline import timeline
import gettext
_ = gettext.gettext
import json
from PIL import Image
import io

st.set_page_config(
    page_title="Antonio - Linha do Tempo",
    page_icon="🏳️‍🌈"
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])
try:
  localizator = gettext.translation('base', localedir='locales', languages=[idioma])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

st.title("Minha História")
with open ('dados_antonio.json', "r", encoding="utf-8") as json_timeline:
    timeline_info = json.load(json_timeline)     
timeline(timeline_info, height=500, )
