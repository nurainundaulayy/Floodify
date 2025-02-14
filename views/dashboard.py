import streamlit as st

# URL of your Looker Studio dashboard
url = "https://lookerstudio.google.com/embed/reporting/26e764f3-726d-41b0-973f-e247489ae1a1/page/vzvNE"  # Replace with your Looker Studio URL

# Use Streamlit's full page width
st.set_page_config(layout="wide")

# Embed the dashboard using an iframe that takes the full screen
st.components.v1.iframe(url, width=1100, height=1600)  # Adjust dimensions if needed
