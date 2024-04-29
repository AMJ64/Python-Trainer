

import streamlit as st
import google.generativeai as genai

st.markdown(open("style.css").read(), unsafe_allow_html=True)
# Configure Google Generative AI
genai.configure(api_key="AIzaSyBzFxnHcrT30nPDNWSJj6xsrbrzQ-wb4Vc")

# Create a text input field for the user's question
user_input = st.text_input("Ask something:")

prompt = f"act as a perfect code generator and your only job is to generate code{user_input}"
# Create a button for the user to submit their question
submit_button = st.button("Submit")

# When the submit button is clicked, generate a response using Google Generative AI
if submit_button:
    model = genai.GenerativeModel("gemini-1.0-pro-latest")
    response = model.generate_content(prompt)
    st.write(response.text)
