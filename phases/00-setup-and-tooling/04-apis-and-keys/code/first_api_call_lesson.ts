//BUILD IT - Step 2

import "dotenv/config";
import Anthropic from "@anthropic-ai/sdk";

async function run() {
  const client = new Anthropic();
  const MODEL = process.env.LLM_MODEL ?? "claude-sonnet-5";

  const response = await client.messages.create({
    model: MODEL,
    max_tokens: 256,
    messages: [{ role: "user", content: "What is a neural network in one sentence?" }],
  });

  console.log(response.content[0].text);
}

run().catch((err) => {
  console.error("Error crítico:", err);
  process.exit(1);
});
