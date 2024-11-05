import os
import google.generativeai as genai

API_KEY = os.getenv("api_key")
genai.configure(api_key=API_KEY)
model =genai.GenerativeModel('gemini-pro')


def get_answer(question):
    response = model.generate_content(question)
    return response.text
    
get_answer('então qual seu nome?')