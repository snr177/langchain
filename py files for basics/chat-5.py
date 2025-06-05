from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
api_key = os.getenv("AZURE_OPENAI_API_KEY") 
model = AzureChatOpenAI(
    azure_deployment=endpoint,
    api_version=api_version,
    temperature=0.7,
    max_tokens=100
)
chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")


print("---- Message History ----")
print(chat_history)