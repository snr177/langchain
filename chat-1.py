from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import os

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
model_name ="gpt-4"

# Initialize the AzureChatOpenAI model
model = AzureChatOpenAI(
    azure_endpoint=endpoint,
    api_version=api_version, 
    model=model_name
)
prompt = input("ASK ANYTHING : ")
result = model.invoke(prompt)

print(result.content)