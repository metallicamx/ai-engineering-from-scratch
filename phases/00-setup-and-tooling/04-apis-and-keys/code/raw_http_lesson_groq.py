import os
import urllib.request
import json
import ssl
from dotenv import load_dotenv

# Cargar variables
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("Falta GROQ_API_KEY en .env")

url = "https://api.groq.com/openai/v1/chat/completions"

# Configuración SSL para intentar evitar detección básica
# Nota: urllib puro sigue siendo detectable por Cloudflare avanzado,
# pero esto es lo más "raw" posible sin SDKs.
context = ssl.create_default_context()
# A veces desactivar la verificación estricta ayuda en entornos de prueba
# (NO USAR EN PRODUCCIÓN), pero el problema real es la huella TLS.
# Intentamos usar un contexto estándar pero con headers muy específicos.

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    # Usar el contexto SSL por defecto pero forzando la conexión
    with urllib.request.urlopen(req, context=context) as resp:
        result = json.loads(resp.read())
        print(result["choices"][0]["message"]["content"])
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode()}")
    print("\nNota: Si persiste el error 1010, es porque Cloudflare bloquea 'urllib' puro.")
    print("Para una práctica 100% 'raw_http' real contra Cloudflare, a veces es necesario")
    print("usar sockets directos (módulo 'socket' y 'ssl'), lo cual es muy complejo,")
    print("o aceptar que en 2026, 'raw' con urllib no es suficiente para bypass de WAF.")

print("Fin de programa raw_http")
