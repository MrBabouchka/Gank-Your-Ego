import requests
import streamlit as st

# Chargement de la clé Riot depuis secrets.toml
RIOT_API_KEY = st.secrets["riot"]["api_key"]

# URL de base pour l'Europe (valable pour la plupart des joueurs EUW/EUNE)
RIOT_SUMMONER_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

def get_puuid_from_summoner(summoner_name):
    """
    Récupère le PUUID (identifiant global unique) à partir du pseudo d'un joueur LoL.
    Retourne un dictionnaire avec puuid, summonerId, level, etc.
    """
    url = f"{RIOT_SUMMONER_URL}{summoner_name}"
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # Contient puuid, summonerId, accountId, etc.
        elif response.status_code == 404:
            return {"error": "Joueur introuvable"}
        else:
            return {"error": f"Erreur Riot API : {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception : {str(e)}"}
