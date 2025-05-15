import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Caminho absoluto para o banco ChromaDB (sempre na raiz do projeto, pasta 'chroma_db')
CHROMA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "chroma_db")
)
PDF_PATH = "/Users/luizfelipebessa/Documents/BessaAI/1chatbot/rag_blackout/data/Apresentacao_Blackout_Producoes.pdf"

EVOLUTION_API_KEY = os.getenv("EVOLUTION_API_KEY")
EVOLUTION_BASE_URL   = os.getenv("EVOLUTION_BASE_URL")
EVOLUTION_INSTANCE_ID   = os.getenv("EVOLUTION_INSTANCE_ID")
WHITELIST = set(os.getenv("WHITELIST", "").split(","))  # vira set de strings