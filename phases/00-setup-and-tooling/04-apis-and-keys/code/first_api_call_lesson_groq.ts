//Para que carge la API KEY deberás ejecutar con npx tsx desde el directorio donde se encuentre el archivo .env con la API KEY

import "dotenv/config"; // 1. Carga las variables desde el archivo .env
import { Groq } from "groq-sdk";

// 2. Inicializa el cliente (busca automáticamente GROQ_API_KEY en process.env)
const client = new Groq();

// 3. Define el modelo (usa uno compatible con Groq)
//const MODEL = process.env.LLM_MODEL ?? "llama-3.1-8b-instant";
//const MODEL = process.env.LLM_MODEL ?? "llama-3.3-70b-versatile";
//const MODEL = process.env.LLM_MODEL ?? "openai/gpt-oss-20b";
const MODEL = process.env.LLM_MODEL ?? "qwen/qwen3.6-27b";

async function main() {
	try {
		const response = await client.chat.completions.create({
			model: MODEL,
			max_tokens: 256,
			messages: [
				{
					role: "user",
					content: "What is a neural network in one sentence?"
				},
			],
		});

		// 4. Accede al contenido con la estructura de Groq/OpenAI
		console.log(response.choices[0].message.content);
	} catch (error) {
		console.error("Error al llamar a la API:", error);
	}
}

main();
