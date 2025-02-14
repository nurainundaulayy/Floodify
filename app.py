import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
detect_page = st.Page(
    page="views/detect.py",
    title="Image Detection",
    icon=":material/smart_toy:"
)
chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot Assistant",
    icon=":material/smart_toy:"
)
dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard Monitoring",
    icon=":material/team_dashboard:"
)
informasi_page = st.Page(
    page="views/informasi.py",
    title="Infromasi",
    icon=":material/info:"
)

# --- NAVIGATION SETUP ---
pg = st.navigation(pages=[home_page, detect_page], expanded=False)

# --- RUN NAVIGATION ---
pg.run()

