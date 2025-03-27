import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_PATH = "db"
PDF_PATH = "/Users/luizfelipebessa/Documents/LambdaAI/1chatbot/rag2-notebook-lambdaai/data/SobreLambdaAI.pdf"