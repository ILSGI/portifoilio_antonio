import streamlit as st 


st.set_page_config(
    page_title="Antonio - sobre mim",
    page_icon="🏳️‍🌈"
)

idioma = st.sidebar.selectbox("escolha o idioma", ['pt', 'en', 'es'])

strings = {
    "en": {
        "titulo": "About me",
        "texto": "Hello, my name is Antonio Moreno. One among the thousands of students at the Sebrae School, but with my own tastes and characteristics that you will see below. Since I was very young, I have enjoyed sports and, above all, the virtual world. Some dreams have been building along with this, and some are still a reality. I believe that through projects and ideas, we can change something, perhaps not the whole world, but a part of it. This is one of the main motivations for wanting to be a better person."
    },
    "pt": {
        "titulo": "Sobre mim",
        "texto": "Prazer, meu nome é Antonio Moreno. Um entre os milhares de estudantes da Escola do Sebrae, mas com suas próprios gostos e características que verão a seguir. Desde muito pequeno gostei de esportes e principalmente o mundo virtual. Alguns sonhos foram se construindo ao longo disso, alguns ainda são uma realidade. Penso que atráves de projetos e ideias, podemos mudar algo, não talvez o mundo inteiro, mas uma parte dele. Isso é uma das principais motivações de querer ser alguém melhor. traduza  para ingles e espanhol"
    },
    "es": {
        "titulo": "Sobre mí",
        "texto": "Hola, mi nombre es Antonio Moreno. Uno entre los miles de estudiantes de la Escuela del Sebrae, pero con mis propios gustos y características que verán a continuación. Desde muy pequeño me gustan los deportes y, sobre todo, el mundo virtual. Algunos sueños se han ido construyendo a lo largo de esto, y algunos todavía son una realidad. Creo que a través de proyectos e ideas, podemos cambiar algo, quizás no el mundo entero, pero sí una parte de él. Esta es una de las principales motivaciones para querer ser una mejor persona."
    }
}

def get_string(idioma, key):
    return strings[idioma][key]

titulo = get_string(idioma,"titulo")
st.title(titulo)

st.subheader("Antonio de Souza Moreno")

texto = get_string(idioma, "texto")
st.write(texto)
