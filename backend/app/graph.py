from typing import TypedDict, Annotated


class GraphState(TypedDict):
    question: Annotated[str, "Question de l'utilisateur"]
    actualites: Annotated[str, "Résultats DuckDuckGo"]
    resume: Annotated[str, "Réponse du LLM"]