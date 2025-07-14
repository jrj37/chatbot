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
## Partie déploiement Azure
### 1. Etape 1
Créer un compte Azure et installer azure CLI

### 2. Etape 2
Tout d'abord il faut stocker les clés API, donc la clé de open-router, pour cela, on utilise Azure key vault

Dans le cadre du projet, il faut stocker les images docker du frontend et du backend
-> Utilisation de Azure Container registry pour les stocker 

Ensuite on a besoins de azure container apps pour utiliser les containers

### 3. Etape 3 
Création des images du backend et frontend en local ou avec github Actions avec une pipeline CI/Cd
Mettre les images dans Azure container registry
 
### 4. Etape 4 
 Déploiement des containers avec azure container apps
 On oublie pas de configurer la clé API de open router avec key vault

 ### 5. Etape 5
Création d'un certificat SSL/TLS avec Azure
 ### 6. Etape 6
 Utilisation de l'url publique pour voir si l'app marche 
 Utilisation de application insight pour log et metrique

## Prérequis nécessaire
Compte azure
Azure CLI
Docker
GIT
Les permissions nécessaire pour modifier les ressources
Role contributor
Pipeline CI/CD avec Github actions
Stockage des clés API avec key vault

## Points d'attention
Sécurité réseau avec HTTPS
regles cores strictes

Accès backend
Restreindre les accès en prod avec authentification

Permission nécessaires 
Role contributor

Les gens qui ont la permission 
Equipe MLOps/DevOPS AI engineer

## Coûts
D'après Azure les prix sont ceci 
Requêtes:
$0.40 par million de requêtes (paiement à l'utilisation) ou $0.34 par million avec une réduction d'un an. 
Mémoire:
Le coût de la mémoire est d'environ $0.0050 par heure (paiement à l'utilisation) et peut être réduit à $0.00414 par heure avec un plan d'économies de 3 ans. 

Donc il faut compter environ $20 pour ACA

pour stocker les images docker $10 
$1 pour azure key vault
Application insight -> $5

## Sécurité
il faut activer HTTPS pour toutes les communications externes
Toutes les clés API dans key vault
CORS en strict donc pas mettre *
corriger les eventuels bug et vulnérabilité

## Gestion API keys et secrets
Ne pas envoyer les clés dans le repos GIT 
Ni mettre directement dans le code
Utilisation de Github secrets pour les credentials azure


## Architecture scalable
[ Utilisateur ]
     ↓ HTTPS
[ Azure Front Door / Application Gateway ]
     ↓
[ Azure Container Apps (Backend + Frontend) ]
     ↓
[ Azure Key Vault ] (gestion sécurisée des secrets)
     ↓
[ Azure Container Registry ] (stockage images Docker)
