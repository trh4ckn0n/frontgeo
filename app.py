import streamlit as st
import requests

# Appliquer un style hacker
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: #00FF00;
        font-family: "Courier New", monospace;
    }
    .stApp {
        background-color: black;
    }
    .stTextInput, .stButton>button {
        background-color: #101010 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
    }
    .stRadio, .stJson {
        color: #00FF00 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <canvas id="matrix" style="position: fixed; top: 0; left: 0; z-index: -1; width: 100vw; height: 100vh;"></canvas>
    <script>
        var c = document.getElementById("matrix");
        var ctx = c.getContext("2d");
        c.height = window.innerHeight;
        c.width = window.innerWidth;
        var letters = "01";
        letters = letters.split("");
        var font_size = 10;
        var columns = c.width / font_size;
        var drops = [];
        for (var x = 0; x < columns; x++) drops[x] = 1;
        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, c.width, c.height);
            ctx.fillStyle = "#00FF00";
            ctx.font = font_size + "px monospace";
            for (var i = 0; i < drops.length; i++) {
                var text = letters[Math.floor(Math.random() * letters.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);
                if (drops[i] * font_size > c.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 33);
    </script>
    """,
    unsafe_allow_html=True
)
# Titre avec effet Anonymous
st.markdown("<h1 style='text-align: center; font-size: 40px;'>👤 Anonymous Tracker</h1>", unsafe_allow_html=True)

# Sélection de la recherche avec un style matrix
st.markdown("<h3>🌎 Trace une IP ou un numéro</h3>", unsafe_allow_html=True)
option = st.radio("Choisis une cible :", ["Adresse IP", "Numéro de téléphone"])

# URL du backend
BACKEND_URL = "https://backgeo.onrender.com"

# Fonction pour interroger l'API et gérer les erreurs
def get_data(endpoint):
    try:
        response = requests.get(endpoint, timeout=10)
        if response.status_code == 200 and response.text.strip():
            return response.json()
        else:
            st.error(f"❌ Erreur {response.status_code} : Impossible de récupérer les données.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Erreur de connexion : {e}")
        return None

# Recherche par adresse IP
if option == "Adresse IP":
    ip = st.text_input("💻 Entrez une adresse IP :")
    
    if st.button("🎯 Traquer"):
        if ip:
            result = get_data(f"{BACKEND_URL}/geolocate/ip/{ip}")
            if result:
                st.json(result)
        else:
            st.warning("⚠️ Veuillez entrer une adresse IP valide.")

# Recherche par numéro de téléphone
elif option == "Numéro de téléphone":
    number = st.text_input("📱 Entrez un numéro (ex: +33612345678) :")
    
    if st.button("📡 Localiser"):
        if number:
            result = get_data(f"{BACKEND_URL}/geolocate/phone/{number}")
            if result:
                st.json(result)
        else:
            st.warning("⚠️ Veuillez entrer un numéro valide.")
