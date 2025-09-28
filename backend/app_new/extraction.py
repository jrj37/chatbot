from langchain_community.document_loaders import WebBaseLoader
from ddgs import DDGS
import re
path = "https://en.wikipedia.org/wiki/Medium_(website)"

def clean_text(path:str) -> str:
    loader = WebBaseLoader(path)
    documents = loader.load()
    cleaned_text = re.sub(r'\s+', ' ', documents[0].page_content.strip())
    return cleaned_text

def browser(query:str)->str:
    with DDGS() as ddgss:
            results = ddgss.text(query, max_results=5)
    return results