import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Caminho absoluto para o banco ChromaDB (sempre na raiz do projeto, pasta 'chroma_db')
CHROMA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "chroma_db")
)
PDF_PATH = "/Users/luizfelipebessa/Documents/BessaAI/1chatbot/rag_blackout/data/Apresentacao_Blackout_Producoes.pdf"