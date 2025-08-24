# Chatbot

Le Chabot IA vise à donner des informations sur les nouveaux projets d'IA générative.
Il intègre un modèle de LLM provenant de Qwen et l'API de DuckDuckGo. 
---

## Structure du projet

Le projet se divise en deux parties : 
La première partie concerne le backend:

- Le modèle **Qwen** est récupéré via **OpenRouter**.
- **DuckDuckGo** est utilisé pour effectuer des recherches internet.
- Pour créer l'agent IA, **LangChain** est implémenté.
- L'ensemble est accessible via une API REST construite avec **FastAPI**.
- Un **Dockerfile** permet de lancer facilement le serveur FastAPI dans un conteneur Docker.

La deuxieme partie concerne cette fois-ci le frontend:
- en react  
- interface inspirée d’iMessage mais en bleu   
- L'interface interagit directement avec fasAPI  
- Dockerfile pour lancer le frontend  


---

## Lancer le projet en local

### 1. Cloner le projet

```bash
git clone https://github.com/jrj37/chatbot.git
cd chatbot
```
### 2. Lancer le projet avec docker

Créer un fichier .secrets.toml dans le dossier backend/config/
Mettre sa clé API openrouter dedans
```
API_KEY_OPEN_ROUTER =  "..."
```
### 3. Lancer le projet avec docker
```bash
docker-compose up --build
```
