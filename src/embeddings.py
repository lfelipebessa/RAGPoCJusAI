from langchain_openai import OpenAIEmbeddings
from src.config import OPENAI_API_KEY

def get_embeddings_function():
    return OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")