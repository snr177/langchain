from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# --- Configuration ---
# It's good practice to define configuration constants at the top
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
MODEL_NAME = "gpt-4"

"""Initializes and returns the AzureChatOpenAI model."""
try:
    model = AzureChatOpenAI(
    api_version=AZURE_OPENAI_API_VERSION, # Use api_version for API version
    azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME, # Use azure_deployment for deployment name
    temperature= 0.7,  # Adjust temperature for response variability
    max_tokens=100,  # Set a limit on the number of tokens in the response
    )
except Exception as e:
    print(f"Error initializing OpenAI model: {e}")
    print("Please check your environment variables and network connection.")

def main(prompt):
    if prompt.lower() == "exit":
        exit()
    response = model.invoke(prompt)
    return response
if __name__ == '__main__':
    st.title("MYGPT") # type: ignore
    prompt = st.text_area("ASK ANYTHING: ") # type: ignore
    response = main(prompt)
    print(st.text_area("AI ASSISTANT:",response.content))# type: ignore