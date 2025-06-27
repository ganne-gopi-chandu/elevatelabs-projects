import streamlit as st
import requests

st.title("🧠 Mental Health Chatbot")

user_input = st.text_input("You:")
if st.button("Send"):
    response = requests.post("http://localhost:5000/chat", json={"message": user_input})
    if response.status_code == 200:
        st.markdown("**Bot:** " + response.json()["reply"])
    else:
        st.warning("API error. Try again.")

