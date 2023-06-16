import openai

from config import OPENAI_API_KEY


class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def classify_sentiment(self, lyrics: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Classify the sentiment in this lyrics:{lyrics}",
            temperature=0,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response["choices"][0]["text"]
