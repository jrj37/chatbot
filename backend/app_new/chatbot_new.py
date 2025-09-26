from extraction import clean_text
from chunk_ranking import chunk,create_vector_store
from prompt import make_prompt
from langchain_core.vectorstores import InMemoryVectorStore
from dynaconf import Dynaconf
from pydantic import BaseModel, Field
from typing import List

# Chargement de la configuration depuis deux fichiers : settings.toml et .secrets.toml
settings = Dynaconf(
    envvar_prefix="DYNACONF",  # Préfixe utilisé pour surcharger les paramètres via les variables d'environnement
    settings_files=[
        '../config/settings.toml',   # Fichier principal de configuration
        '../config/.secrets.toml'    # Fichier contenant les secrets (API keys, etc.)
    ],
)

class Chatbot(BaseModel):
    settings: object
    cleaned_text: str = Field(..., min_length=1)
    question: str = Field(..., min_length=1)

    def create_context(self,vectorstore:InMemoryVectorStore):
        #self.question = "Donne moi la date de création de medium"
        context = vectorstore.similarity_search(self.question, k=3)
        return context

    def setup(self) -> str:
        chunks = chunk(self.cleaned_text)
        vector_store = create_vector_store(chunks,self.settings.API_TOGETHER_EMBEDDING)
        context = self.create_context(vector_store)
        message = make_prompt(context,self.question,settings)
        return message 
    
if __name__ == "__main__":
    cleaned_text = clean_text("https://en.wikipedia.org/wiki/Medium_(website)")
    chatbot = Chatbot(settings=settings,cleaned_text=cleaned_text,question="Donne moi la date de création de medium")
    print(chatbot.setup())
