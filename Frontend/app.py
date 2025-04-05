# frontend/app.py

import streamlit as st
import requests

st.title("Study Routine Coach & Motivation Chatbot")

# Chat Section
st.header("Chat with Your Study Coach")
user_input = st.text_input("What is your study goal? (e.g., prepare for an exam, learn a new skill)")
if st.button("Get Study Plan"):
    # Replace the backend URL if needed; here it is assumed to be accessible via 'backend'
    response = requests.post("http://backend:5000/generate-routine", json={"user_input": user_input})
    if response.status_code == 200:
        routine = response.json().get("routine")
        st.write("Your Personalized Study Plan:")
        st.write(routine)
    else:
        st.error("There was an error generating your study plan.")

# You can add more interactive elements or instructions as needed.
