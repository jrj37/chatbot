"""
# backend/app/web_search.py
"""
from langgraph.graph import StateGraph, END
from ddgs import DDGS
from datetime import date
from app.graph import GraphState

class NewsSearcher:
    """
    Composant chargé d'effectuer une recherche web via DuckDuckGo
    à partir d'une question utilisateur, et d'en extraire un texte exploitable.
    """

    def __call__(self, state: GraphState) -> GraphState:
        """
        Recherche des actualités à partir de la question et met à jour l'état.

        Args:
            state (GraphState): Dictionnaire contenant la question.

        Returns:
            GraphState: État mis à jour avec les actualités ou un message d'erreur.
        """
        today_str = date.today().strftime("%d %B %Y")
        query = f"{state['question']} la semaine du {today_str}"

        try:
            # Utilise le contexte DDGS pour faire une recherche
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=15)

                # Si aucun résultat n'est trouvé
                if not results:
                    return {**state, "actualites": "Aucun résultat trouvé pour cette recherche."}

                # Formate les résultats en texte brut concaténé
                texte = "\n\n".join([
                    f"{r['title']}\n{r['href']}\n{r['body']}" for r in results
                ])

                return {**state, "actualites": texte}

        except Exception as e:
            # Gestion d'erreur générique, utile si le moteur échoue ou est inaccessible
            return {**state, "actualites": f"Erreur lors de la recherche d’actualités : {str(e)}"}
