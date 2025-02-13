
import streamlit as st
import google.generativeai as ai


system_prompt = """You are an AI-powered Python Code Reviewer.
Your primary role is to analyze submitted Python code, identify potential bugs, suggest improvements,
 and provide optimized and corrected code snippets."""

api_key = st.secrets["AIzaSyAVMS7VfIcpm_B6d-SYWiU_GVwjbdj3HB8"]
ai.configure(api_key=api_key)

model = ai.GenerativeModel(model_name="models/gemini-1.5-flash",system_instruction = system_prompt)

st.title(":speech_balloon: An AI Code Reviewer")
query = st.text_area("Enter Your Python code Here...")
btn_click = st.button("Generate")

if btn_click:
    response = model.generate_content(query)
    st.write(response.text)
