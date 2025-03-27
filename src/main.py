from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
import openai
import os
from dotenv import load_dotenv
from langchain.schema.document import Document
#from get_embedding_function import get_embeddings_function
from langchain.vectorstores.chroma import Chroma

# Carregar variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Criar modelo de linguagem (LLM)
llm = ChatOpenAI(model = "gpt-3.5-turbo", api_key = OPENAI_API_KEY)

# 1. Processando os Documentos
def load_documents():
    # Carregar o PDF
    document_loader = PyPDFLoader("/Users/luizfelipebessa/Documents/LambdaAI/1chatbot/rag2-notebook-lambdaai/data/SobreLambdaAI.pdf") # Endereço do PDF
    return document_loader.load()

def split_documents(documents: list[Document]):
    # Dividir texto em trechos menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
        )
    return text_splitter.split_documents(documents)


def calculate_cunkcs_ids(chunks):
    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

    

# print(f"Documento carregado e dividido em {len(texts)} partes.")

# 2. Criando a Base de Conhecimento (Vetores + FAISS)
# Base de conhecimento
def embeddings():
    # Criando embeddings
    embeddings = OpenAIEmbeddings(api_key = OPENAI_API_KEY, model="text-embedding-3-small")

    return embeddings


def add_to_chroma(chunks: list[Document]):
    # Criando banco chroma
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embeddings_function()
    )
    db.add_documents(new_chunks, ids=new_chunk_ids)
    db.persist()

# 3. Prompt
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de IA especializado na empresa LambdaAI."
     "Responda com precisão de forma clara e objetiva. Se não souber a resposta, diga que não sabe." 
     "Use os seguintes trechos de contexto recuperado para responder à pergunta: \n\n{context}"),
    ("human", "{chat_history}"),
    ("human", "{input}")
])


# 4. Criando a Cadeia de Resolução de Perguntas

# Criar o QA Chain
question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
qa_chain = create_retrieval_chain(retriever, question_answer_chain)
# 5. Criando o Chatbot

'''
def chatbot():
    print("\n🤖 Chatbot RAG iniciado! Pergunte algo sobre a LambdaAI.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        question = input("Você: ")

        if question.lower() in ["sair", "exit", "quit"]:
            print("🔚 Chat encerrado.")
            break

        # 🔍 Buscar resposta
        result = qa_chain.invoke({"input": question})
        
        # 📝 Mostrar resposta
        print("\nChatbot:", result["answer"], "\n")
'''

def obter_resposta(pergunta, historico):
    """Função que recebe uma pergunta e retorna a resposta do chatbot"""
    
    # 🔹 Formatar histórico para que seja uma string legível
    historico_formatado = "\n".join([f"{msg['role']}: {msg['content']}" for msg in historico])

    # 🔍 Invocar o chatbot com o histórico formatado
    result = qa_chain.invoke({
        "input": pergunta,
        "chat_history": historico_formatado
    })

    return result["answer"]
