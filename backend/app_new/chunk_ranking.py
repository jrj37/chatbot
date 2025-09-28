from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_together import TogetherEmbeddings
from app_new.extraction import clean_text

def chunk(cleaned_text:str):
    textesplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    chunks = textesplitter.split_text(cleaned_text)
    return chunks

def create_vector_store(api_key:str) -> InMemoryVectorStore:
    embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5", max_retries=5, api_key=api_key)
    vectorstore = InMemoryVectorStore(embeddings)
    return vectorstore
