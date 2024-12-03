from flask import Flask, request, jsonify
import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gemini_ia import responder_mensagem

app = Flask(__name__)

@app.route('/getAnswer', methods=['POST'])
def getAnswer():
    data = request.get_json()
    question = data['question']
    answer = responder_mensagem(question)

    resposta = answer.rstrip()
    resposta = re.sub(r'[\*\n\"]+', '', resposta)
    return jsonify({'answer': resposta})


if __name__ == '__main__':
    app.run(debug=True)