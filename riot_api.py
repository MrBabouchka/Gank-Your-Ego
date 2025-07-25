import os
import requests

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

REGION_ROUTING = {
    "euw1": "europe",
    "eun1": "europe",
    "na1": "americas",
    "br1": "americas",
    "la1": "americas",
    "la2": "americas",
    "oc1": "sea",
    "kr": "asia",
    "jp1": "asia",
    "tr1": "europe",
    "ru": "europe",
}


def get_puuid_from_summoner(summoner_name: str, region: str) -> dict:
    """Retourne le PUUID et niveau d’un joueur LoL."""
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return {
            "puuid": data["puuid"],
            "summonerLevel": data["summonerLevel"]
        }
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"error": "Invocateur introuvable. Vérifie le pseudo et la région."}
        return {"error": f"Erreur API Riot (code {response.status_code}) : {e}"}
    except Exception as e:
        return {"error": f"Erreur interne : {e}"}


def get_last_game_id(puuid: str, region: str) -> str | dict:
    """Retourne l’ID de la dernière partie du joueur."""
    routing = REGION_ROUTING.get(region)
    if not routing:
        return {"error": "Région non supportée."}

    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        game_ids = response.json()
        if not game_ids:
            return {"error": "Aucune partie trouvée pour ce joueur."}
        return game_ids[0]
    except Exception as e:
        return {"error": f"Impossible de récupérer la dernière partie : {e}"}


def get_match_data(match_id: str, region: str) -> dict:
    """Retourne les données détaillées de la partie."""
    routing = REGION_ROUTING.get(region)
    if not routing:
        return {"error": "Région non supportée."}

    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Impossible de récupérer les données du match : {e}"}
