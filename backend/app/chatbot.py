from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from ddgs import DDGS
import requests
from app.graph import GraphState
from datetime import date


class NewsSummarizer:
    def __init__(self,settings) -> None:
        self.settings = settings

    def __call__(self, state: GraphState) -> GraphState:
        texte = state["actualites"]
        question = state["question"]
        today_str = date.today()
        day = today_str.strftime("%d %B %Y")

        if not texte.strip():
            return {**state, "resume": "Aucune actualité trouvée."}

        prompt_user = (
            f"Tu trouveras ci-dessous les résultats d'une recherche web réalisée le {day}\n"
            f"A partir des principales sources d’information technologique (TechCrunch, The Verge, Medium, etc.).\n"
            f"Sujet de la recherche :\n"
            f"« {question} »\n\n"
            f"Résultats trouvés :\n"
            f"{texte}\n\n"
            f"À partir de ces éléments, peux-tu donner 3 exemples concrets avec leur source et date ?"
        )

        payload = {
            "model": self.settings.DEFAULT.MODEL_NAME,
            "messages": [
                {"role": "system", "content": "Tu synthétises des recherches web pour répondre de manière structurée, concise et sourcée."},
                {"role": "user", "content": prompt_user}
            ]
        }

        headers = {
            "Authorization": f"Bearer {self.settings.API_KEY_OPEN_ROUTER}",
            "Content-Type": "application/json"
        }

        response = requests.post(self.settings.DEFAULT.OPEN_ROUTER_URL, json=payload, headers=headers)

        if response.status_code == 200:
            message = response.json()["choices"][0]["message"]["content"]
            return {**state, "resume": message}
        else:
            raise Exception(f"Erreur OpenRouter : {response.status_code} – {response.text}")