import os
import asyncio
import aiohttp
from tenacity import retry, wait_exponential, stop_after_attempt

API_URL = os.getenv("LLM_API_URL")  # e.g., https://api.openai.com/v1/responses
API_KEY = os.getenv("LLM_API_KEY")
MODEL   = os.getenv("LLM_MODEL", "your-model")
TIMEOUT = int(os.getenv("LLM_TIMEOUT", "60"))

class LLMClient:
    def __init__(self, api_url: str = None, api_key: str = None, model: str = None):
        self.api_url = api_url or API_URL
        self.api_key = api_key or API_KEY
        self.model = model or MODEL
        if not self.api_url or not self.api_key:
            raise RuntimeError("Set LLM_API_URL and LLM_API_KEY in your environment (.env).")

    @retry(wait=wait_exponential(multiplier=1, min=1, max=10), stop=stop_after_attempt(5))
    async def call(self, payload: dict):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=headers, json=payload, timeout=TIMEOUT) as r:
                r.raise_for_status()
                return await r.json()

    async def chat(self, messages, **params):
        payload = {
            "model": self.model,
            "messages": messages,
            **params
        }
        return await self.call(payload)

# Example usage:
# messages = [{"role":"system","content":"You are helpful"}, {"role":"user","content":"Hello"}]
# resp = asyncio.run(LLMClient().chat(messages, temperature=0))
# print(resp)
