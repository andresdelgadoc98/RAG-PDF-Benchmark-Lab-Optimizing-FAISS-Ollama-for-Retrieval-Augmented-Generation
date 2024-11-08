from .functions import list_pdf_files
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from uuid import uuid4
from dotenv import load_dotenv
import os
from .extract_text import extract_text_pdfplumber

load_dotenv()
embedding_model = os.getenv("EMBEDDING_MODEL")
chunk_size = os.getenv("CHUNK_SIZE")
FOLDER_NAME_FILES = os.getenv("FOLDER_NAME_FILES")
FOLDER_NAME_EMBBEDINGS = os.getenv("FOLDER_NAME_EMBBEDINGS")
chunk_overlap = os.getenv("chunk_overlap")
embedding = OllamaEmbeddings(model=embedding_model)

def save_chunks():
    chunker = RecursiveCharacterTextSplitter(chunk_size=int(chunk_size),chunk_overlap=int(chunk_overlap))
    file_names = list_pdf_files(FOLDER_NAME_FILES)

    for file in file_names:
        print(file)
        page_text, metadata = extract_text_pdfplumber(file)
        chunks = chunker.create_documents(texts=page_text,metadatas=metadata)
        if not os.path.exists(FOLDER_NAME_EMBBEDINGS):
            chunks_vectorstore = FAISS.from_documents(chunks, embedding=embedding)
            chunks_vectorstore.save_local(FOLDER_NAME_EMBBEDINGS)
        else:
            vector_store = FAISS.load_local(FOLDER_NAME_EMBBEDINGS, embedding, allow_dangerous_deserialization=True)
            uuids = [str(uuid4()) for _ in range(len(chunks))]
            vector_store.add_documents(documents=chunks, ids=uuids)
            vector_store.save_local(FOLDER_NAME_EMBBEDINGS)

    return True