from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os,time
load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
model_name ="gpt-4"
model = AzureChatOpenAI(
    api_version= api_version,
    azure_endpoint= endpoint,
    model= model_name
)
messages = [
    SystemMessage("Act like a jarvis and give me accurate results"),
    HumanMessage("Get me the info about the recent google I/O event and what are the main things to notice")
]
result = model.invoke(messages)
print("AI responding...!")
time.sleep(5)
print(result.content)