
from langchain_core.prompts import PromptTemplate
import requests

from dynaconf import Dynaconf

# Chargement de la configuration depuis deux fichiers : settings.toml et .secrets.toml
settings = Dynaconf(
    envvar_prefix="DYNACONF",  # Préfixe utilisé pour surcharger les paramètres via les variables d'environnement
    settings_files=[
        '../config/settings.toml',   # Fichier principal de configuration
        '../config/.secrets.toml'    # Fichier contenant les secrets (API keys, etc.)
    ],
)

def make_prompt(context:str,question:str,settings:object) -> str:
    prompt = PromptTemplate(template="voici des extraits de documents liés à ta requête : {context}\n\nPeux-tu répondre à la question suivante : {question} ?",
                            input_variables=["context","question"])
    final_prompt = prompt.format(context=context, question=question)
    # Payload à envoyer à l'API OpenRouter (modèle de langage)
    payload = {
        "model": settings.DEFAULT.MODEL_NAME,
        "messages": [
        {"role": "system", "content": "Tu synthétises des recherches web pour répondre de manière structurée, concise et sourcée. Tu réponds qu'a l'aide du contexte fournis."},    
        {"role": "user", "content": final_prompt}
        ]
    }

    # En-têtes HTTP, incluant la clé API pour l’authentification
    headers = {
    "Authorization": f"Bearer {settings.API_KEY_OPEN_ROUTER}",
    "Content-Type": "application/json"
    }

    # Requête POST vers l’API OpenRouter pour obtenir une réponse du modèle
    response = requests.post(settings.DEFAULT.OPEN_ROUTER_URL, json=payload, headers=headers)
    message = response.json()["choices"][0]["message"]["content"]
    print("Réponse du modèle :")
    return message