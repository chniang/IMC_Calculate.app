import streamlit as st

# Appliquer le style CSS pour modifier les couleurs
st.markdown(
    """
    <style>
    body {
        background-color: #0b1d3a;
        color: white;
    }
    .stApp {
        background-color: #0b1d3a;
    }
    h1, h2, h3, h4, h5, h6, p, label, div {
        color: white !important;
    }
    .stButton>button {
        background-color: #1f6f8b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stNumberInput>div>div>input {
        background-color: #ffffff15;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre de l'application
st.title("Bienvenue dans l'application de calcule de l'IMC")

# Entrée pour le poids (en kg)
weight = st.number_input("Renseigner votre poids en Kg", min_value=0.0, format="%.2f")

# Boutons radio pour le format de la taille
status = st.radio("Sélectionner le format de votre taille :", ('cm', 'mettre', 'feet'))

# Prise de taille avec décimales autorisées
if status == 'cm':
    height = st.number_input('Taille en centimètres', min_value=0.0, format="%.2f")
    try:
        IMC = weight / ((height / 100) ** 2)
    except:
        st.text("Entrer un bon format de taille")

elif status == 'mettre':
    height = st.number_input('Taille en mètres', min_value=0.0, format="%.2f")
    try:
        IMC = weight / (height ** 2)
    except:
        st.text("Entrer un bon format de taille")

else:
    height = st.number_input('Taille en feet', min_value=0.0, format="%.2f")
    try:
        IMC = weight / ((height / 3.28) ** 2)
    except:
        st.text("Entrer un bon format de taille")

# Bouton pour lancer le calcul
if st.button('Calculer IMC'):
    st.text("Votre IMC est {:.2f}".format(IMC))
    
    if IMC < 16:
        st.error("Tu es extrêmement maigre")
    elif 16 <= IMC < 18.5:
        st.warning("Tu es maigre")
    elif 18.5 <= IMC < 25:
        st.success("Votre corpulence est normale")
    elif 25 <= IMC < 30:
        st.warning("Vous êtes en surpoids")
    else:
        st.error("Vous êtes en obésité")
