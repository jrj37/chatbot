"""
# backend/app/agent.py
"""
from langgraph.graph import StateGraph, END
from datetime import date
from app.web_search import NewsSearcher
from app.chatbot import NewsSummarizer
from app.graph import GraphState

class Agent:
    """
    Agent intelligent combinant une recherche web et un résumé automatique
    via un graphe d'étapes LangGraph.
    """

    def __init__(self, params) -> None:
        """
        Initialise l'agent avec les composants de recherche et de résumé.

        Args:
            params: Objet de configuration contenant les clés d’API et modèles.
        """
        self.searcher = NewsSearcher()              # Composant de recherche web (ex. via DuckDuckGo)
        self.summarizer = NewsSummarizer(params)    # Composant de résumé basé sur un LLM
        self.graph = self._build_graph()            # Construction du graphe LangGraph
        self.params = params                        # Stocke les paramètres pour usage ultérieur

    def _build_graph(self):
        """
        Construit le graphe d'exécution LangGraph avec deux étapes :
        - Recherche d’actualités
        - Résumé des résultats

        Returns:
            Graph: Graphe compilé prêt à être invoqué.
        """
        builder = StateGraph(GraphState)                # Initialisation du graphe avec le type d'état
        builder.add_node("Recherche", self.searcher)    # Étape 1 : recherche web
        builder.add_node("Résumé", self.summarizer)     # Étape 2 : résumé de la recherche
        builder.set_entry_point("Recherche")            # Point d'entrée du graphe
        builder.add_edge("Recherche", "Résumé")         # Transition : recherche → résumé
        builder.add_edge("Résumé", END)                 # Fin du graphe après le résumé
        return builder.compile()                        # Compilation du graphe

    def run(self, question: str) -> str:
        """
        Exécute le graphe pour une question donnée.

        Args:
            question (str): Sujet ou question de l'utilisateur.

        Returns:
            str: Résumé généré par le modèle LLM.
        """
        # Invoque le graphe avec l’état initial contenant la question
        result = self.graph.invoke({"question": question})

        # Affiche un log lisible côté console avec la date
        print(f"\n Résumé du {date.today().strftime('%d %B %Y')} :\n")

        # Retourne uniquement la partie "resume" du résultat
        return result["resume"]
