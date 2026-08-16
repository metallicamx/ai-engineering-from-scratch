import os
import json
from dotenv import load_dotenv
from curl_cffi import requests

# Cargar variables de entorno
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("No se encontró GROQ_API_KEY en el archivo .env")

url = "https://api.groq.com/openai/v1/chat/completions"

# Headers estándar
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Datos de la solicitud
data = {
    "model": os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}

# SOLUCIÓN: Usar requests de curl_cffi con impersonación de Chrome
# Esto clona el handshake TLS real de Chrome, evitando el error 1010
response = requests.post(
    url,
    headers=headers,
    json=data,
    impersonate="chrome124"  # Clave del éxito: imita Chrome 124
)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}: {response.text}")

print("\nFin programa groq con curl_cffi")
