from langchain_community.document_loaders import WebBaseLoader
import re
path = "https://en.wikipedia.org/wiki/Medium_(website)"

def clean_text(path:str) -> str:
    loader = WebBaseLoader("https://en.wikipedia.org/wiki/Medium_(website)")
    documents = loader.load()
    cleaned_text = re.sub(r'\s+', ' ', documents[0].page_content.strip())
    return cleaned_text