import streamlit as st
import requests

st.title("Géolocalisation IP & Numéro")

option = st.selectbox("Choisir une option", ["IP", "Numéro de téléphone"])

if option == "IP":
    ip = st.text_input("Entrez une IP")
    if st.button("Rechercher"):
        response = requests.get(f"https://mon-backend.onrender.com/geolocate/ip/{ip}")
        st.json(response.json())

elif option == "Numéro de téléphone":
    number = st.text_input("Entrez un numéro")
    if st.button("Rechercher"):
        response = requests.get(f"https://mon-backend.onrender.com/geolocate/phone/{number}")
        st.json(response.json())
