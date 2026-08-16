import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def test_openai_connection():
    # Obtener la clave desde el entorno
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ Error: No se encontró la variable de entorno OPENAI_API_KEY.")
        print("Asegúrate de crear un archivo .env con tu clave.")
        return

    try:
        # Inicializar el cliente (usa la clave del entorno automáticamente si se configura así,
        # pero la pasamos explícitamente para mayor claridad en este test)
        client = OpenAI(api_key=api_key)

        # Realizar una solicitud de prueba mínima
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # O el modelo que tengas disponible (ej. gpt-4o)
            messages=[
                {"role": "user", "content": "Responde solo con la palabra 'Conectado' si recibes este mensaje."}
            ],
            max_tokens=5
        )

        # Extraer y mostrar la respuesta
        contenido = response.choices[0].message.content
        print(f"✅ ¡Conexión exitosa! Respuesta de la API: {contenido}")

    except Exception as e:
        print(f"❌ Error de conexión o clave inválida: {e}")

if __name__ == "__main__":
    test_openai_connection()   
