import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Portfolio - Serigne Fallou Diop", layout="wide")

# Titre principal
st.title(" Portfolio de Serigne Fallou Diop")
st.subheader("Technicien Supérieur en Géomatique | Licence 3 Géographie - UCAD")

# Menu latéral
menu = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Formation", "Compétences", "Expériences", "Projets", "Contact"]
)

# ACCUEIL
if menu == "Accueil":
    st.header(" À propos de moi")
    st.write("""
    Je suis Technicien Supérieur en Géomatique et étudiant en Licence 3 de Géographie à l’Université Cheikh Anta Diop de Dakar.
    
    Passionné par :
    - Les Systèmes d’Information Géographique (SIG)
    - L’analyse spatiale
    - La télédétection
    - La gouvernance territoriale
    
    Mon objectif est d’utiliser la géomatique pour contribuer au développement territorial et à la planification stratégique au Sénégal.
    """)

# FORMATION
elif menu == "Formation":
    st.header(" Formation")
    
    st.write("###  BTS Géomatique")
    st.write("Centre Sectoriel de Formation Professionnelle aux Métiers du BTP (G15)")
    
    st.write("###  Licence 3 Géographie")
    st.write("Université Cheikh Anta Diop de Dakar (UCAD)")

# COMPÉTENCES
elif menu == "Compétences":
    st.header("🛠 Compétences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("SIG & Cartographie")
        st.write("- ArcGIS")
        st.write("- QGIS")
        st.write("- Jointure spatiale")
        st.write("- Analyse spatiale")
        st.write("- Production cartographique")
    
    with col2:
        st.subheader("Autres compétences")
        st.write("- Python (bases)")
        st.write("- Collecte de données terrain")
        st.write("- Télédétection")
        st.write("- Traitement d’images (Pix4D, Agisoft)")
        st.write("- Recensement et enquêtes")

# EXPÉRIENCES
elif menu == "Expériences":
    st.header(" Expériences")
    
    st.write("###  Agent Enquêteur - ANSD")
    st.write("""
    Participation au Recensement National de la Population du Sénégal.
    - Collecte de données
    - Localisation des ménages
    - Travail de terrain
    """)

# PROJETS
elif menu == "Projets":
    st.header(" Projets académiques")
    
    st.write("###  Cartographie Agricole Intelligente")
    st.write("""
    Projet basé sur l'utilisation des SIG pour :
    - L'analyse des terres agricoles
    - L’étude de l’impact climatique
    - L’amélioration de la planification territoriale
    """)
    
    st.write( "### Analyse spatiale des infrastructures rurales")
    st.write("""
    Utilisation des SIG pour améliorer l’accessibilité
    aux services publics (eau, routes, électricité).
    """)

# CONTACT
elif menu == "Contact":
    st.header(" Contact")
    
    st.write(" Dakar, Sénégal")
    st.write(" Email : serignefallou@email.com")
    st.write(" Téléphone : +221 781263530")
    
    st.success("Disponible pour stage et collaboration en Géomatique.")