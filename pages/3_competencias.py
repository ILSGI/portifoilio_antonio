import streamlit as st 
import gettext
_ = gettext.gettext

st.set_page_config(
    page_title="Antonio - competencias",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "titulo": "Competencies",
        "gestao de trafego": "Through various projects and studies, I have become highly capable and efficient in managing a company's traffic.",
        "gestao de midias sociais": "In traffic management, I was able to create a strong brand image, attracting respect and credibility through social media.",
        "ingles": "english",
        "espanhol": "Spanish"
    },
    "pt": {
        "titulo": "Competências",
        "gestao de trafego": "por diversos projetos e estudos, me tornei muito capaz e eficiente na gestão de trafego de um empresa.",
        "gestao de midias sociais": "justo a gestão de trafego, consegui gerar uma boa visão da marca atraindo respeito e credibilidade por meio das redes sociais",
        "ingles": "inglês",
        "espanhol": "espanhol"
    },
    "es": {
        "titulo": "Competencias",
        "gestao de trafego": "Through various projects and studies, I have become highly capable and efficient in managing a company's traffic. This graph represents the growth of a company after starting to work with me.",
        "gestao de midias sociais": "En la gestión del tráfico, logré crear una sólida imagen de marca, atrayendo respeto y credibilidad a través de las redes sociales.",
        "ingles": "Inglés",
        "espanhol": "Español"
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

with st.expander("gestão de trafego"):
    gestao de trafego = get_string(idioma, "gestao de trafego")
    st.write(gestao de trafego)
    
with st.expander("gestão de midias sociais"):
    gestao de trafego = get_string(idioma, "gestao de trafego")
    st.write(gestao de trafego)
    
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
    
