import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Gank Your Ego", page_icon="🧠", layout="centered")

# Titre principal
st.title("🧠 Gank Your Ego")
st.write("Bienvenue dans ton coach LoL brutalement honnête.")

# --- ESPACE UTILISATEUR ---
st.markdown("### 🎮 Analyse ta dernière game")

# Champ pour entrer le pseudo
summoner_name = st.text_input("Entre ton pseudo League of Legends")

# Bouton de lancement
if st.button("Analyser ma dernière game"):
    if not summoner_name:
        st.warning("Merci de renseigner ton pseudo d'abord.")
    else:
        # Placeholder d'analyse (mock)
        st.info(f"Analyse en cours pour **{summoner_name}**...")
        st.success("Archétype détecté : 🛡️ Support protecteur (mock)")
        st.markdown("👉 _Tu joues safe, mais t’oublies parfois de ward. On en parle._")

