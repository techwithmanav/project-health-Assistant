import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


PDF_FILE = "data/nutrition.pdf"
VECTOR_DB = "vector_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_rag():

    if not os.path.exists(PDF_FILE):
        raise FileNotFoundError(
            f"Nutrition PDF not found: {PDF_FILE}"
        )

    document = PyPDFLoader(PDF_FILE).load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(document)

    embedding = get_embeddings()

    db = FAISS.from_documents(
        chunks,
        embedding
    )

    db.save_local(VECTOR_DB)

    return len(chunks)


@st.cache_resource
def load_rag():

    if not os.path.exists(VECTOR_DB):
        create_rag()

    embedding = get_embeddings()

    db = FAISS.load_local(
        VECTOR_DB,
        embedding,
        allow_dangerous_deserialization=True
    )

    return db
