# Image to text model

import streamlit as st
import google.generativeai as genai
import os
import textwrap
from PIL import Image
import pathlib


genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

headers = {"authorization": st.secrets["GOOGLE_API_KEY"],
          "content-type": "application/json"}

st.set_page_config(page_title="✅ Gemini")

st.header("🎯Gemini Image to Text Application 🖼️ 📝 🔰")
input=st.text_input("📒 Input Prompt: ",key="input")
uploaded_file = st.file_uploader("📋 Upload an image...", 
                                 type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Do the Magic")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
