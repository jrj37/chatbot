from langgraph.graph import StateGraph, END
from datetime import date
from app.web_search import NewsSearcher
from app.chatbot import NewsSummarizer
from app.graph import GraphState

class Agent:
    def __init__(self,params) -> None:
        self.searcher = NewsSearcher()
        self.summarizer = NewsSummarizer(params)
        self.graph = self._build_graph()
        self.params = params

    def _build_graph(self):
        builder = StateGraph(GraphState)
        builder.add_node("Recherche", self.searcher)
        builder.add_node("Résumé", self.summarizer)
        builder.set_entry_point("Recherche")
        builder.add_edge("Recherche", "Résumé")
        builder.add_edge("Résumé", END)
        return builder.compile()

    def run(self, question: str) -> str:
        result = self.graph.invoke({"question": question})
        print(f"\n📰 Résumé du {date.today().strftime('%d %B %Y')} :\n")
        return result["resume"]