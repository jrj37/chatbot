from app_new.extraction import clean_text, browser
from app_new.chunk_ranking import chunk,create_vector_store
from app_new.prompt import make_prompt
from langchain_core.vectorstores import InMemoryVectorStore
from dynaconf import Dynaconf
from pydantic import BaseModel, Field
from typing import List

class Chatbot(BaseModel):
    settings: object
    question: str = Field(..., min_length=1)

    def create_dataset(self):
        res = browser(self.question)
        print(res)
        l_text = []
        vector_store = create_vector_store(self.settings.API_TOGETHER_EMBEDDING)
        for website in res:
            cleaned_text = clean_text(website['href'])
            vector_store.add_texts(chunk(cleaned_text))
        return vector_store

    def create_context(self,vectorstore:InMemoryVectorStore):
        #self.question = "Donne moi la date de création de medium"
        context = vectorstore.similarity_search(self.question, k=3)
        return context

    def setup(self) -> str:
        vector_store = self.create_dataset()
        context = self.create_context(vector_store)
        message = make_prompt(context,self.question,self.settings)
        return message 