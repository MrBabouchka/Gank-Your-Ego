def analyze_match_for_player(match_data, puuid):
    """
    Extrait les données principales du joueur ciblé dans une game.
    Retourne un résumé structuré : champion, KDA, rôle, score de vision, etc.
    """
    try:
        # 1. Trouver le joueur concerné
        participant = None
        for p in match_data["metadata"]["participants"]:
            if p == puuid:
                participant_index = match_data["metadata"]["participants"].index(p)
                participant = match_data["info"]["participants"][participant_index]
                break

        if not participant:
            return {"error": "Joueur non trouvé dans cette partie."}

        # 2. Extraire les infos clés
        data = {
            "champion": participant["championName"],
            "role": participant["teamPosition"],
            "kills": participant["kills"],
            "deaths": participant["deaths"],
            "assists": participant["assists"],
            "kda": round((participant["kills"] + participant["assists"]) / max(1, participant["deaths"]), 2),
            "cs": participant["totalMinionsKilled"] + participant["neutralMinionsKilled"],
            "vision_score": participant["visionScore"],
            "win": participant["win"],
            "dmg_to_champions": participant["totalDamageDealtToChampions"]
        }

        return data

    except Exception as e:
        return {"error": f"Erreur lors de l'analyse : {str(e)}"}
