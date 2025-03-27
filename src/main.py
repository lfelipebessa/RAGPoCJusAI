import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.vectorstore import carregar_pdf, dividir_em_chunks, salvar_no_chroma
from src.chain import build_chain

# Pergunta de teste
PERGUNTA_TESTE = "Qual o número de telefone da LambdaAI?"

def main():
    print("📄 Etapa 1: Carregando documento...")
    documentos = carregar_pdf()

    print("✂️ Etapa 2: Fazendo split...")
    chunks = dividir_em_chunks(documentos)

    print("💾 Etapa 3: Salvando chunks no ChromaDB...")
    salvar_no_chroma(chunks)

    print("🤖 Etapa 4: Criando a chain e fazendo uma pergunta...")
    rag_chain = build_chain()

    resposta = rag_chain.invoke({
        "input": PERGUNTA_TESTE,
        "chat_history": ""
    })

    print("\n✅ Resposta:")
    print(resposta["answer"])

if __name__ == "__main__":
    main()