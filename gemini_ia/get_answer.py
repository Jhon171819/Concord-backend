import os
import google.generativeai as genai
import os
import spacy

nlp = spacy.load("modelos\\modelo_treinado") 

API_KEY = os.getenv("api_key")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')






def get_answer(question):
    response = model.generate_content(question)
    return response.text


def responder_mensagem(mensagem):
    doc = nlp(mensagem)
    resposta = get_answer(mensagem)

    if doc.cats['nome'] > 0.5:
        resposta = "Meu nome é Concord"
        
    return resposta
