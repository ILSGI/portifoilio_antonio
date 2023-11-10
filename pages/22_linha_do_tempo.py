import streamlit as st
from streamlit_timeline import timeline
import json
from PIL import Image
import io

st.set_page_config(
    page_title="Antonio - Linha do Tempo",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "titulo": "timeline",
    },
    "pt": {
        "titulo": "linha do tempo",
    },
    "es": {
        "titulo": "línea de tiempo",
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

if idioma == "en" : 
    with open ('dados_antonio_en.json', "r", encoding="utf-8") as json_timeline:
        timeline_info = json.load(json_timeline)     
elif idioma == "es" :
    with open ('dados_antonio_es.json', "r", encoding="utf-8") as json_timeline:
        timeline_info = json.load(json_timeline) 
elif idioma == "pt" : 
    with open ('dados_antonio_pt.json', "r", encoding="utf-8") as json_timeline:
        timeline_info = json.load(json_timeline) 


timeline(timeline_info, height=500, )
