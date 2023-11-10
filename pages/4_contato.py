import streamlit as st 


st.set_page_config(
    page_title="Antonio - contato",
    page_icon=""
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "contato": "contact",
        "midias sociais": "social midia"
    },
    "pt": {
        "contato": "contato",
        "midias sociais": "midias sociais"
    },
    "es": {
        "contato": "Contacto",
        "midias sociais": "redes sociales"
    }
}
def get_string(idioma, key):
    return strings[idioma][key]

contato = get_string(idioma,"contato")
midias_sociais = get_string(idioma,"midias sociais")

st.title(contato)
st.subheader("📞: +55 (31) 984717322")
st.subheader("✉️: moreno1707@gmail.com")
st.title(midias_sociais)
st.subheader("📷: @as.morenoo")

st.text("https://github.com/ILSGI/portifoilio_antonio/tree/main")
