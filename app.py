# Text Generation Model
from dotenv import load_dotenv
load_dotenv() # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_AP_KEY"))

# Function to get Gemini Response

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialoze the Streamlit App
st.set_page_config(page_title="QnA Demo")

st.header("Gemini Application")

input = st.text_input("Enter your Query: ", key = "input")
submit = st.button("Ask your Question")

# When Submitted...

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is: ")
    st.write(response)
