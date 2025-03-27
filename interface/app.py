import streamlit as st
import sys
import os

# Adicionar src ao sys.path para garantir importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importando a função corretamente
from src.chatbot import obter_resposta

# Configurar título da aplicação
st.set_page_config(page_title="Chatbot LambdaAI", layout="centered")

# Interface do chatbot
st.title("🤖 Chatbot LambdaAI")
st.write("Pergunte algo sobre a LambdaAI!")

# Inicializar histórico da conversa
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Exibir mensagens anteriores no chat
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Caixa de input para perguntas
pergunta = st.chat_input("Digite sua pergunta...")

# Se houver pergunta, processar
if pergunta:
    # Adicionar pergunta ao histórico
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # ✅ Passando o histórico corretamente
    resposta = obter_resposta(pergunta, st.session_state.mensagens)

    # Adicionar resposta ao histórico
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)