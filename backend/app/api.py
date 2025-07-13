from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import Agent

class Api:
    def __init__(self,settings:object) -> None:
        self.app = FastAPI()
        origins = [
            "http://localhost:3000",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.settings = settings
        self.register_routes()

    def register_routes(self):
        @self.app.get("/agent")    
        def ask_agent(prompt: str):
            agent = Agent(self.settings)
            resume = agent.run(prompt)
            
            return {"response": resume}
