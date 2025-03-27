import streamlit as st
import requests

# Titre de l'application
st.title("🔍 Géolocalisation IP & Numéro de téléphone")

# Sélection de la recherche
option = st.radio("Que souhaitez-vous rechercher ?", ["Adresse IP", "Numéro de téléphone"])

# URL du backend
BACKEND_URL = "https://backgeo.onrender.com"

# Fonction pour interroger l'API et gérer les erreurs
def get_data(endpoint):
    try:
        response = requests.get(endpoint, timeout=10)
        
        # Afficher le statut HTTP et la réponse brute pour debug
        st.write(f"Statut HTTP: {response.status_code}")
        st.write("Réponse brute:", response.text)
        
        if response.status_code == 200 and response.text.strip():
            return response.json()
        else:
            st.error(f"Erreur {response.status_code} : Impossible de récupérer les données.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion : {e}")
        return None

# Recherche par adresse IP
if option == "Adresse IP":
    ip = st.text_input("Entrez une adresse IP")
    
    if st.button("Rechercher"):
        if ip:
            result = get_data(f"{BACKEND_URL}/geolocate/ip/{ip}")
            if result:
                st.json(result)
        else:
            st.warning("Veuillez entrer une adresse IP valide.")

# Recherche par numéro de téléphone
elif option == "Numéro de téléphone":
    number = st.text_input("Entrez un numéro de téléphone avec l'indicatif pays (ex: +33612345678)")
    
    if st.button("Rechercher"):
        if number:
            result = get_data(f"{BACKEND_URL}/geolocate/phone/{number}")
            if result:
                st.json(result)
        else:
            st.warning("Veuillez entrer un numéro valide.")
