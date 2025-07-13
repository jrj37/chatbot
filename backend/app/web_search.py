from langgraph.graph import StateGraph, END
from ddgs import DDGS
from datetime import date
from app.graph import GraphState

class NewsSearcher:
    def __call__(self, state: GraphState) -> GraphState:
        today_str = date.today().strftime("%d %B %Y")
        query = f"{state['question']} la semaine du {today_str}"

        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=15)
            texte = "\n\n".join([f"{r['title']}\n{r['href']}\n{r['body']}" for r in results])
        
        return {**state, "actualites": texte}
