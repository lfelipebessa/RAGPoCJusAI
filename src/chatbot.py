import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.chain import build_chain

rag_chain = build_chain()

def obter_resposta(pergunta, historico):
    historico_formatado = "\n".join([f"{msg['role']}: {msg['content']}" for msg in historico])
    resposta = rag_chain.invoke({
        "input": pergunta,
        "chat_history": historico_formatado
    })
    return resposta["answer"]