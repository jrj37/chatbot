"""
# backend/app/graph.py
"""
from typing import TypedDict, Annotated

class GraphState(TypedDict):
    """
    Représente l'état partagé entre les différentes étapes d'un graphe LangGraph.

    Attributs :
        question (str)     : La question posée par l'utilisateur.
        actualites (str)   : Les résultats de recherche récupérés (ex : via DuckDuckGo).
        resume (str)       : Le résumé ou la réponse générée par un LLM (modèle de langage).
    """
    question: Annotated[str, "Question de l'utilisateur"]
    actualites: Annotated[str, "Résultats DuckDuckGo"]
    resume: Annotated[str, "Réponse du LLM"]
