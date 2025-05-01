import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_casos(historia_usuario):
    prompt = f"""
Eres un ingeniero QA experto. Analiza esta historia de usuario y genera:
1. Casos de prueba manuales detallados (título, pasos, resultado esperado).
2. Escenarios Gherkin para automatización BDD.

Historia:
{historia_usuario}
    """

    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )

    return respuesta.choices[0].message.content
