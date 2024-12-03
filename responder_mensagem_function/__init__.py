import logging
import spacy
from gemini_ia import get_answer
import azure.functions as func

nlp = spacy.load("modelos/modelo_treinado") 

def responder_mensagem(mensagem):
    doc = nlp(mensagem)
    resposta = get_answer(mensagem)

    if doc.cats.get('nome', 0) > 0.5:
        resposta = "Meu nome é Concord"
    
    return resposta

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processando uma nova requisição.")

    try:
        # Obter o conteúdo da mensagem enviada via POST
        req_body = req.get_json()
        mensagem = req_body.get("mensagem")
        
        if mensagem:
            resposta = responder_mensagem(mensagem)
            return func.HttpResponse(resposta, status_code=200)
        else:
            return func.HttpResponse("Mensagem não fornecida.", status_code=400)
    except Exception as e:
        logging.error(f"Erro ao processar a mensagem: {e}")
        return func.HttpResponse("Erro no servidor.", status_code=500)
