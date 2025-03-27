from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente de IA especializado na empresa LambdaAI. Use o seguinte contexto para responder à pergunta com clareza. Se não souber, diga que não sabe.\n\n{context}"),
        ("human", "{chat_history}"),
        ("human", "{input}")
    ])