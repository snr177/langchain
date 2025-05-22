from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
import os
from dotenv import load_dotenv

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
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME, # Use azure_deployment for deployment name
    model=MODEL_NAME
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
    prompt = input("ASK ANYTHING: ")
    print(main(prompt))