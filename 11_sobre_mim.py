import streamlit as st 


st.set_page_config(
    page_title="Antonio - sobre mim",
    page_icon="🏳"
)
strings = {
    "en": {
        "titulo": "About me",
        "texto": "Hello, my name is Antonio. I am passionate about the digital world, and as a young traffic manager born in 2007, my job is to transform businesses through the digital realm. I can help you grow your passion for business and turn it into success."
    },
    "pt": {
        "titulo": "Sobre mim",
        "texto": "olá meu nome Antonio, sou apaixonado pelo mundo digital e sou um jovem gestor de trefego nascido no ano de 2007, meu trabalho é transformar negocios por meio do mundo digital, posso ajuda-lo a crescer cada paixão por negocios e transforma-lo em um sucesso!"
    },
    "es": {
        "titulo": "Sobre mí",
        "texto": "Hola, mi nombre es Antonio. Soy apasionado por el mundo digital y, como joven gestor de tráfico nacido en 2007, mi trabajo es transformar negocios a través del mundo digital. Puedo ayudarte a hacer crecer tu pasión por los negocios y convertirla en éxito."
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

st.subheader("Antonio de Souza Moreno")

texto = get_string(idioma, "texto")
st.write(texto)
