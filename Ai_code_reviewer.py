import streamlit as st
import google.generativeai as ai

# Load API Key securely
api_key = st.secrets["GOOGLE_API_KEY"]

# Configure API key
ai.configure(api_key=api_key)

# Define system prompt
system_prompt = """You are an AI-powered Python Code Reviewer.
Your primary role is to analyze submitted Python code, identify potential bugs, 
suggest improvements, and provide optimized and corrected code snippets."""

# ✅ FIX: Proper way to define the GenerativeModel
model = ai.GenerativeModel(model_name="gemini-1.5-flash")  # Fix here

# Streamlit UI
st.title(":speech_balloon: AI Code Reviewer")
query = st.text_area("Enter Your Python code Here...")
btn_click = st.button("Generate")

if btn_click:
    response = model.generate_content(query)  # Generate response
    st.write(response.text)
