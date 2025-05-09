from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.prompts import get_prompt
from src.embeddings import get_embeddings_function
from src.config import OPENAI_API_KEY, CHROMA_PATH


def build_chain():
    retriever = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings_function()
    ).as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
    prompt = get_prompt()
    
    question_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=question_chain
)
    
    return rag_chain