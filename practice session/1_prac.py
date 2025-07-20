from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr
import sys

# Load environment variables from .env file
load_dotenv()

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Only create the model if we have the necessary credentials
if azure_endpoint and deployment_name and api_version and api_key:
    try:
        model = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_version=api_version,
            api_key=SecretStr(api_key),
        )
        print("Model initialized successfully")
        response = model.invoke("HI")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"Error initializing model: {e}")
