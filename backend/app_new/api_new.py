"""
# backend/app/api.py
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_new.chatbot_new import Chatbot
from dynaconf import Dynaconf

class Api:
    def __init__(self, settings: object) -> None:
        """
        Initialise l'application FastAPI avec les paramètres donnés.

        Args:
            settings (object): Objet de configuration utilisé pour initialiser l'agent.
        """
        self.app = FastAPI()

        # Origines autorisées pour les requêtes CORS (par exemple depuis un frontend React)
        origins = [
            "http://localhost:3000",
        ]

        # Ajout du middleware CORS pour permettre les requêtes cross-origin
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,            # Domaines autorisés
            allow_credentials=True,           # Autoriser les cookies/headers d'authentification
            allow_methods=["*"],              # Autoriser toutes les méthodes HTTP (GET, POST, etc.)
            allow_headers=["*"],              # Autoriser tous les headers
        )

        self.settings = settings  # Stocke les paramètres pour l'agent
        self.register_routes()    # Enregistre les routes de l'API

    def register_routes(self):
        """
        Enregistre les routes de l'application, notamment la route /agent.
        """
        @self.app.get("/agent")
        def ask_agent(prompt: str):
            """
            Route GET qui permet d'interroger l'agent IA avec un prompt.

            Args:
                prompt (str): Message/question envoyé à l'agent.

            Returns:
                dict: Réponse générée par l'agent, au format {"response": réponse_textuelle}
            """
            # Création d'une instance de l'agent avec les paramètres
            chatbot = Chatbot(settings=self.settings,question=prompt)

            # Exécution du prompt par l'agent
            resume = chatbot.setup()
            print(resume)

            # Retourne la réponse dans un dictionnaire JSON
            return {"response": resume}
