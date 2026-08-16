#BUILD IT - Step 4

import os
import urllib.request
import json

# 1. Función manual para leer .env sin librerías externas
def load_env_manual(ruta=".env"):
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo {ruta}")
    
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            # Ignorar líneas vacías o comentarios
            if not linea or linea.startswith("#"):
                continue
            # Separar clave y valor
            if "=" in linea:
                clave, valor = linea.split("=", 1)
                os.environ[clave.strip()] = valor.strip()

# 2. Cargar las variables antes de usarlas
load_env_manual()

url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
}

body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "claude-sonnet-5"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode("utf-8")

req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        if "content" in result and len(result["content"]) > 0:
            print(result["content"][0]["text"])
except urllib.error.HTTPError as e:
    print(f"Error HTTP: {e.code} - {e.reason}")
    print(e.read().decode())
except Exception as e:
    print(f"Error: {e}")   
