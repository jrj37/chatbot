from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_together import TogetherEmbeddings
from extraction import clean_text

def chunk(cleaned_text:str):
    textesplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    chunks = textesplitter.split_text(cleaned_text)
    return chunks

def create_vector_store(chunks:list) -> InMemoryVectorStore:
    embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5", max_retries=5, api_key="6a17ef0b1f9674dd2c4223929420d2789bdce8dd488bbd40ba9f7d895c4a5ccc")
    vectorstore = InMemoryVectorStore(embeddings)
    vectorstore.add_texts(chunks)
    return vectorstore
    question = "Donne moi la date de création de medium"
    context = vectorstore.similarity_search(question, k=3)
    return context

def create_context(vectorstore:InMemoryVectorStore):
    question = "Donne moi la date de création de medium"
    context = vectorstore.similarity_search(question, k=3)
    return context

create_vector_store(chunk(clean_text("https://en.wikipedia.org/wiki/Medium_(website)")))