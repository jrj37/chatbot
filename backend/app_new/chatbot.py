from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_together import TogetherEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_together import ChatTogether
import requests
import json
import re
from dynaconf import Dynaconf

# Chargement de la configuration depuis deux fichiers : settings.toml et .secrets.toml
settings = Dynaconf(
    envvar_prefix="DYNACONF",  # Préfixe utilisé pour surcharger les paramètres via les variables d'environnement
    settings_files=[
        '../config/settings.toml',   # Fichier principal de configuration
        '../config/.secrets.toml'    # Fichier contenant les secrets (API keys, etc.)
    ],
)

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Medium_(website)")
documents = loader.load()
cleaned_text = re.sub(r'\s+', ' ', documents[0].page_content.strip())

textesplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
chunks = textesplitter.split_text(cleaned_text)
embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5", max_retries=5, api_key="6a17ef0b1f9674dd2c4223929420d2789bdce8dd488bbd40ba9f7d895c4a5ccc")
vectorstore = InMemoryVectorStore(embeddings)
vectorstore.add_texts(chunks)
question = "sais-tu ce qu'est Medium ? Peux-tu me donner un résumé de ce site web ?"
context = vectorstore.similarity_search(question, k=3)
prompt = PromptTemplate(template="voici des extraits de documents liés à ta requête : {context}\n\nPeux-tu répondre à la question suivante : {question} ?",
                        input_variables=["context","question"])
final_prompt = prompt.format(context=context, question=question)
# Payload à envoyer à l'API OpenRouter (modèle de langage)
payload = {
    "model": settings.DEFAULT.MODEL_NAME,
    "messages": [
    {"role": "system", "content": "Tu synthétises des recherches web pour répondre de manière structurée, concise et sourcée."},    
    {"role": "user", "content": final_prompt}
    ]
}

# En-têtes HTTP, incluant la clé API pour l’authentification
headers = {
"Authorization": f"Bearer {settings.API_KEY_OPEN_ROUTER}",
"Content-Type": "application/json"
}

# Requête POST vers l’API OpenRouter pour obtenir une réponse du modèle
response = requests.post(settings.DEFAULT.OPEN_ROUTER_URL, json=payload, headers=headers)
message = response.json()["choices"][0]["message"]["content"]
print("Réponse du modèle :")
print(message)
