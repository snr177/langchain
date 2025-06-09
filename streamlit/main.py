import streamlit as st
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
endpoint = "https://models.github.ai/inference"
model = "meta/Llama-3.2-90B-Vision-Instruct"
token = os.getenv("GITHUB_TOKEN")
def chatbot(prompt):
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(str(token)),
    )

    response = client.complete(
        messages=[
            SystemMessage("Act as jarvis and answer the questions"),
            UserMessage(prompt),
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model
    )

    return response.choices[0].message.content

st.title("MYGPT") # type: ignore
prompt = st.text_area("ASK ANYTHING: ") # type: ignore
response = chatbot(prompt)
print(st.text_area("AI ASSISTANT:",response))# type: ignore