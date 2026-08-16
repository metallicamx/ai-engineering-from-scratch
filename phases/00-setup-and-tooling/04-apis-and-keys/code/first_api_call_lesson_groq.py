import os
from dotenv import load_dotenv  # 1. Importar cargador de .env
from groq import Groq

# 2. Cargar el archivo .env ANTES de acceder a las variables
load_dotenv() 

# Ahora sí buscará en el archivo .env si no está en el sistema
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

#MODEL = "llama-3.1-8b-instant" 
#MODEL = "llama-3.3-70b-versatile" 
#MODEL = "openai/gpt-oss-20b" 
MODEL = "qwen/qwen3.6-27b" 

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "What is a neural network in one sentence?"}
    ],
    max_tokens=256
)

print(response.choices[0].message.content)   
