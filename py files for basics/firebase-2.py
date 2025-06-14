import os
import time
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import AzureChatOpenAI

# Load environment variables from .env file
load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
project_id = os.getenv("PROJECT_ID")
session_id = os.getenv("SESSION_ID")
collection_name = os.getenv("COLLECTION_NAME")

# Initialize the Azure OpenAI model for chat
model = AzureChatOpenAI(
    azure_deployment=endpoint,
    api_version=api_version
)

# Initialize Firestore client and chat history storage
client = firestore.Client(project=project_id)
chat_history = FirestoreChatMessageHistory(
    session_id=session_id,  # type:ignore Unique session for each chat
    collection=collection_name,  # type:ignore  Firestore collection name
    client=client
)

def instructions():
    """
    Launches an interactive command-line chatbot using Azure OpenAI and Firestore for chat history.
    
    Features:
        - Displays ASCII art from a file at startup.
        - Prompts the user to choose an action: 'chat', 'history', or 'exit'.
        - 'chat': Allows the user to enter a query, sends it to the AI, and displays the response.
        - 'history': Shows the chat history from Firestore.
        - 'exit': Exits the chatbot gracefully with messages.
    
    Environment Variables Required:
        - AZURE_OPENAI_DEPLOYMENT_NAME
        - AZURE_OPENAI_API_VERSION
        - PROJECT_ID
        - SESSION_ID
        - COLLECTION_NAME
    """
    # Main chatbot loop
    user = input("Choose an action ('chat', 'history', 'exit'): ").strip().lower()
    while True:
        if user == "exit":
            # Graceful exit with user-friendly messages
            print("PLEASE WAIT...!")
            time.sleep(1)
            print("ABORTING")
            time.sleep(3)
            print("Exiting the bot")
            time.sleep(2)
            print("EXITED")
            print("THANK YOU FOR YOUR TIME...!")
            break
        elif user == "history":
            # Show chat history from Firestore
            print("PLEASE WAIT...!")
            time.sleep(5)
            print("PAST MESSAGES:")
            print(chat_history)
            user = input("Choose an action ('chat', 'history', 'exit'): ").strip().lower()
        elif user == "chat":
            # Start a new chat interaction
            print("OKAY, CONTINUE TO CHAT..!")
            print("Initializing...")
            time.sleep(1)
            print("All set!")
            print("Ready...")
            print()
            try:
                user_input = input("ENTER YOUR QUERY: ")
                if user_input.lower() == "exit":
                    print("Exiting the chat...")
                    user = input("Choose an action ('chat', 'history', 'exit'): ").strip().lower()
                else:
                    # Add user message to chat history
                    chat_history.add_user_message(message=user_input)
                    # Get AI response from Azure OpenAI
                    ai_message = model.invoke(chat_history.messages)
                    # Add AI response to chat history
                    chat_history.add_ai_message(message=ai_message.content)  # type: ignore
                    print("AI:", ai_message.content)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            # Handle invalid input
            print("Invalid option. Please choose 'chat', 'history', or 'exit'.")
            user = input("Choose an action ('chat', 'history', 'exit'): ").strip().lower()

# Display ASCII art at startup (optional)
try:
    with open('./ascii-text-art.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ASCII art file not found. Skipping art display.")

# Show function docstring and start the chatbot
print(instructions.__doc__)
instructions()
