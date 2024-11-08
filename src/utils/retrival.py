from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
load_dotenv()
embedding_model = os.getenv("EMBEDDING_MODEL")
embedding = OllamaEmbeddings(model=embedding_model)
number_chunks = os.getenv('NUMBER_CHUNKS')
FOLDER_NAME_EMBBEDINGS = os.getenv("FOLDER_NAME_EMBBEDINGS")

def retrival(user_question):

    chunk_vectorstore = FAISS.load_local(FOLDER_NAME_EMBBEDINGS, embedding, allow_dangerous_deserialization=True)
    chunk_retriever = chunk_vectorstore.as_retriever(search_kwargs={"k": int(number_chunks)})
    results = chunk_retriever.invoke(user_question)
    return results