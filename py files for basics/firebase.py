# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/
import os
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import AzureChatOpenAI
"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project
    - Copy the project ID
3. Create a Firestore database in the Firebase project
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""

load_dotenv()

# Setup Firebase Firestore
PROJECT_ID = os.getenv("PROJECT_ID")  # Replace with your Firebase project ID
SESSION_ID = os.getenv("SESSION_ID")  # Replace with your session ID=
COLLECTION_NAME = os.getenv("COLLECTION_NAME")  # Replace with your Firestore collection name
# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID, # type: ignore
    collection=COLLECTION_NAME, # type: ignore
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History: \n", chat_history)

# Initialize Chat Model
model = AzureChatOpenAI(
    azure_deployment= os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version="2023-05-15",
)

print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)# type: ignore

    print(f"AI: {ai_response.content}")