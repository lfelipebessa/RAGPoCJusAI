from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.embeddings import get_embeddings_function
from src.config import PDF_PATH, CHROMA_PATH

def carregar_pdf():
    loader = PyPDFLoader(PDF_PATH)
    return loader.load()

def dividir_em_chunks(documentos):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(documentos)

def salvar_no_chroma(chunks):
    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings_function(),
        persist_directory=CHROMA_PATH
    )
    db.persist()
    return db