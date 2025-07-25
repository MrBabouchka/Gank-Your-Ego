import streamlit as st

# Configuration générale
st.set_page_config(page_title="Gank Your Ego", page_icon="🧠", layout="centered")

st.title("🧠 Gank Your Ego")
st.markdown("**Le coach LoL brutalement honnête.**")

# --- SESSION STATE pour le pseudo et la page active ---
if "summoner_name" not in st.session_state:
    st.session_state["summoner_name"] = ""

if "page" not in st.session_state:
    st.session_state["page"] = None

# --- CHAMP PSEUDO ---
pseudo = st.text_input("🎮 Entre ton pseudo League of Legends", value=st.session_state["summoner_name"])
st.session_state["summoner_name"] = pseudo.strip()

# --- VERROU : pseudo obligatoire pour débloquer les boutons ---
if not st.session_state["summoner_name"]:
    st.warning("Merci de renseigner ton pseudo pour accéder aux fonctionnalités.")
    st.stop()

# --- MENU PRINCIPAL ---
st.markdown("## 🚀 Que veux-tu faire ?")
col1, col2 = st.columns(2)

with col1:
    if st.button("Analyser ma dernière game"):
        st.session_state["page"] = "last_game"
    if st.button("Draft intelligente"):
        st.session_state["page"] = "draft"

with col2:
    if st.button("Analyser mon profil global"):
        st.session_state["page"] = "profile"
    if st.button("Plan d'entraînement personnalisé"):
        st.session_state["page"] = "training"

# --- SÉPARATEUR ---
st.markdown("---")

# --- AFFICHAGE DYNAMIQUE PAR PAGE ---
if st.session_state["page"] == "last_game":
    st.subheader("📊 Analyse de ta dernière game")
    st.info(f"Analyse en cours pour **{st.session_state['summoner_name']}**...")
    st.success("Mock : 🛡️ Support protecteur")
    st.markdown("_Tu joues safe, mais t’oublies parfois de ward. On en parle._")

elif st.session_state["page"] == "profile":
    st.subheader("🧠 Analyse de ton profil (10 dernières games)")
    st.info(f"Analyse en cours pour **{st.session_state['summoner_name']}**...")
    st.success("Mock : 🧨 Jungler explosif")
    st.markdown("_Tu joues pour toi, et c’est souvent clutch. Mais tu pings pas, et tu tilt si le mid roam pas._")

elif st.session_state["page"] == "draft":
    st.subheader("📋 Draft intelligente")
    st.markdown("_Fonctionnalité à venir. Prépare-toi à bannir intelligemment (et pas juste Teemo)._")

elif st.session_state["page"] == "training":
    st.subheader("💪 Plan d'entraînement personnalisé")
    st.markdown("_Bientôt dispo : un plan sur 3 games pour devenir plus clutch que Faker._")

elif st.session_state["page"] is None:
    st.info("Sélectionne une action dans le menu ci-dessus pour commencer.")