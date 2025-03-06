import spacy

from treinamentos.treinamento import treinamento
from gemini_ia import get_answer

nlp = spacy.load("modelos\\modelo_treinado") 

def responder_mensagem(mensagem):
    doc = nlp(mensagem)
    resposta = get_answer(mensagem)

    if doc.cats['nome'] > 0.5:
        resposta = "Meu nome é Concord"
    
    return resposta

question = input("faça uma pergunta: ")

print(responder_mensagem(question))

