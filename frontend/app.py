import streamlit as st
import requests
from PIL import Image

import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.ocr import extract_text_from_image

API_URL = "http://127.0.0.1:8000/generate_reply"

def get_ai_reply(chat_text):
    response = requests.post(API_URL, json={"chat_text": chat_text})
    if response.status_code == 200:
        return response.json().get("reply", "Error in AI response")
    return "Error contacting API"

st.title("AI Chat Reply Assistant")
uploaded_file = st.file_uploader("Upload Chat Screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Screenshot", use_column_width=True)
    extracted_text = extract_text_from_image(image)
    st.text_area("Extracted Chat", extracted_text, height=150)
    
    if st.button("Generate AI Reply"):
        ai_reply = get_ai_reply(extracted_text)
        st.text_area("Suggested Reply", ai_reply, height=100)
