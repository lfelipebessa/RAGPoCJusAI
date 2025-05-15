# Entrypoint do Flask
# app.py
import flask
from flask_cors import CORS
import os, sys, json
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from chatbot import obter_resposta
from wppAPI import EvolutionAPI


evo = EvolutionAPI()
app = flask.Flask(__name__)
load_dotenv()

CORS(app)

# memória de histórico por número
chat_histories: dict[str, list[dict]] = {}


@app.route("/webhook", methods=["POST"])
def webhook():
    print("✅ Webhook recebido!")
    print(flask.request.json)
    #return flask.jsonify(data)

    try:
        data = flask.request.json
        print("📥 Payload recebido:")
        print(data)

        message = data['data']['message']['conversation']
        instance = data['instance']
        instance_key = data['apikey']
        sender_number = data['data']['key']['remoteJid'].split("@")[0]  # ✅ isso pega o número do cliente

        print(f"👤 Mensagem de: {sender_number} | Conteúdo: {message}")


    except Exception as e:
        return flask.jsonify({"error": f"estrutura inválida: {e}"}), 400

    WHITELIST = {"556196088951", "996182880999"}
    if sender_number not in WHITELIST:
        print(f"Numero fora da Whitelist: {sender_number}")
        return flask.jsonify({"status": "ignorado"}), 200
    
    try:
        # Histórico
        hist = chat_histories.setdefault(sender_number, [])
        hist.append({"role": "user", "content": message})
        
        response = obter_resposta(message, hist)
        hist.append({"role": "assistant", "content": response})

        # Geração da resposta com RAG
        response = obter_resposta(message, hist)
    
    except Exception as e:
        print(f"❌ Erro ao gerar resposta com RAG: {e}")
        return flask.jsonify({"error": str(e)}), 500

    # Envio pela Evolution-API
    try:
        evo.send_msg(response, instance, instance_key, sender_number)
        print("📤 Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem pela EvolutionAPI: {e}")
        return flask.jsonify({"error send_msg": str(e)}), 500

    return flask.jsonify({"response": response})



if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))  # troquei para 5050 por conflito na 5000
    print(f"🚀 Servidor iniciado em http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)