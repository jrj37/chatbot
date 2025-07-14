"""
# backend/app/main.py
"""
from app.api import Api               # Importe la classe Api contenant l'application FastAPI
from dynaconf import Dynaconf        # Importe Dynaconf pour gérer la configuration de manière flexible

# Chargement de la configuration depuis deux fichiers : settings.toml et .secrets.toml
settings = Dynaconf(
    envvar_prefix="DYNACONF",  # Préfixe utilisé pour surcharger les paramètres via les variables d'environnement
    settings_files=[
        '../config/settings.toml',   # Fichier principal de configuration
        '../config/.secrets.toml'    # Fichier contenant les secrets (API keys, etc.)
    ],
)

# Initialisation de l'API avec les paramètres chargés
api = Api(settings)

# Exposition de l'application FastAPI (objet app) pour le serveur ASGI (ex: Uvicorn)
app = api.app
