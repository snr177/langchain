import os
import requests

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('XAI_API_KEY')}"
}
payload = {
    "messages": [
        {
            "role": "user",
            "content": "Provide me a digest of world news in the last 24 hours."
        }
    ],
    "search_parameters": {
        "mode": "auto"
    },
    "model": "grok-3-latest"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())