# main.py

import os
import requests
from dotenv import load_dotenv

# 1️⃣ Charger les variables d'environnement
load_dotenv()
API_KEY = os.getenv("MARKETSTACK_API_KEY")
print("Clé API :", API_KEY)

# 2️⃣ Choisir l'action à récupérer
symbol = "AAPL"

# 3️⃣ Construire l'URL de l'API
url = f"http://api.marketstack.com/v1/eod?access_key={API_KEY}&symbols={symbol}"

# 4️⃣ Envoyer la requête à l'API
response = requests.get(url)

# 5️⃣ Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()  # Convertir en JSON
    print(f"Données récupérées pour {symbol} :")
    print(data)
else:
    print(f"Erreur {response.status_code} lors de la récupération des données")
