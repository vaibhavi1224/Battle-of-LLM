from openai import OpenAI
import os
import requests
from transformers import pipeline

client = OpenAI(api_key="our_openai_key")
hf_headers = {"Authorization": "Bearer our_hf_key"}

def summarize_text(text, model_name, closed=True):
    if closed:
        prompt = f"Summarize this article clearly and concisely:\n\n{text}"
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    else:
        hf_model = model_name
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{hf_model}",
            headers=hf_headers,
            json={"inputs": text}
        )
        if response.status_code == 200:
            return response.json()[0]["summary_text"]
        else:
            return "⚠️ Summary failed."
