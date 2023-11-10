import streamlit as st 
import pandas as pf

st.set_page_config(
    page_title="Antonio - competencias",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "titulo": "Competencies",
        "gestaodetrafego": "Through various projects and studies, I have become highly capable and efficient in managing a company's traffic.",
        "gestaodemidiassociais": "In traffic management, I was able to create a strong brand image, attracting respect and credibility through social media.",
        "ingles": "english",
        "espanhol": "Spanish"
    },
    "pt": {
        "titulo": "Competências",
        "gestaodetrafego": "por diversos projetos e estudos, me tornei muito capaz e eficiente na gestão de trafego de um empresa.",
        "gestaodemidiassociais": "justo a gestão de trafego, consegui gerar uma boa visão da marca atraindo respeito e credibilidade por meio das redes sociais",
        "ingles": "inglês",
        "espanhol": "espanhol"
    },
    "es": {
        "titulo": "Competencias",
        "gestaodetrafego": "Through various projects and studies, I have become highly capable and efficient in managing a company's traffic. This graph represents the growth of a company after starting to work with me.",
        "gestaodemidiassociais": "En la gestión del tráfico, logré crear una sólida imagen de marca, atrayendo respeto y credibilidad a través de las redes sociales.",
        "ingles": "Inglés",
        "espanhol": "Español"
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

with st.expander("gestão de trafego"):
    gestaodetrafego = get_string(idioma, "gestaodetrafego")
    st.write(gestaodetrafego)
    
with st.expander("gestao de midias sociais"):
    gestaodemidiassociais = get_string(idioma, "gestaodemidiassociais")
    st.write(gestaodemidiassociais)
    
st.text("Inglés")
Inglés_df_data = [["total","B1"],["comprensión lectora","B2"],["comprensión auditiva","B2"],["expresión escrita","B1"],["expresión oral","B1"]]
def createDataframe(Inglés_df_data: [[int]]) -> pd.DataFrame:
    column_names = ['Inglés', 'nivel de idioma']
    sla = pd.DataFrame(Inglés_df_data, columns=column_names)
    return sla
df_es = createDataframe(Inglés_df_data)
st.table(df_es)

st.text("españhol")
espanhol_df_data = [["total","B1"],["comprensión lectora","B2"],["comprensión auditiva","B2"],["expresión escrita","B1"],["expresión oral","B1"]]
def createDataframe(espanhol_df_data: [[int]]) -> pd.DataFrame:
    column_names = ['españhol', 'nivel de idioma']
    sla = pd.DataFrame(espanhol_df_data, columns=column_names)
    return sla
df_es = createDataframe(espanhol_df_data)
st.table(df_es)
    
