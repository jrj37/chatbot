"""
# backend/app/chatbot.py
"""
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from ddgs import DDGS
import requests
from app.graph import GraphState
from datetime import date


class NewsSummarizer:
    def __init__(self, settings) -> None:
        """
        Initialise le résumeur d'actualités.

        Args:
            settings: Objet de configuration contenant les paramètres pour l'API OpenRouter.
        """
        self.settings = settings

    def __call__(self, state: GraphState) -> GraphState:
        """
        Fonction principale appelée automatiquement lors de l'exécution de l'étape LangGraph.

        Args:
            state (GraphState): Dictionnaire contenant les actualités ('actualites') et la question posée ('question').

        Returns:
            GraphState: État mis à jour avec un résumé structuré sous la clé 'resume'.
        """
        texte = state["actualites"]  # Texte brut contenant les résultats d'une recherche web
        question = state["question"]  # Sujet ou question sur les actualités
        today_str = date.today()
        day = today_str.strftime("%d %B %Y")  # Date actuelle formatée

        # Si aucun texte n’est présent, on retourne un message d’absence d’actualité
        if not texte.strip():
            return {**state, "resume": "Aucune actualité trouvée."}

        # Prompt envoyé au modèle pour qu’il génère une synthèse structurée
        prompt_user = (
            f"Tu trouveras ci-dessous les résultats d'une recherche web réalisée le {day}\n"
            f"A partir des principales sources d’information technologique (TechCrunch, The Verge, Medium, etc.).\n"
            f"Sujet de la recherche :\n"
            f"« {question} »\n\n"
            f"Résultats trouvés :\n"
            f"{texte}\n\n"
            f"À partir de ces éléments, peux-tu donner 3 exemples concrets avec leur source et date ?"
        )

        # Payload à envoyer à l'API OpenRouter (modèle de langage)
        payload = {
            "model": self.settings.DEFAULT.MODEL_NAME,
            "messages": [
                {"role": "system", "content": "Tu synthétises des recherches web pour répondre de manière structurée, concise et sourcée."},
                {"role": "user", "content": prompt_user}
            ]
        }

        # En-têtes HTTP, incluant la clé API pour l’authentification
        headers = {
            "Authorization": f"Bearer {self.settings.API_KEY_OPEN_ROUTER}",
            "Content-Type": "application/json"
        }

        # Requête POST vers l’API OpenRouter pour obtenir une réponse du modèle
        response = requests.post(self.settings.DEFAULT.OPEN_ROUTER_URL, json=payload, headers=headers)

        # Si la requête réussit, on extrait et retourne la réponse textuelle
        if response.status_code == 200:
            message = response.json()["choices"][0]["message"]["content"]
            return {**state, "resume": message}
        else:
            # Sinon, on lève une exception avec le code d’erreur et le message retourné
            raise Exception(f"Erreur OpenRouter : {response.status_code} – {response.text}")
