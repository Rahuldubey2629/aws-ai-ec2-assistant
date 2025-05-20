from openai import OpenAI
from src.config import settings

class OpenAIHandler:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate_content(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=settings.temperature,
            max_tokens=2000
        )
        return response.choices[0].message.content
