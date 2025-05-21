import os
import time
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage

# Load environment variables
load_dotenv()

# --- Configuration ---
# It's good practice to define configuration constants at the top
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
MODEL_NAME = "gpt-4"

# --- Helper Functions ---

def display_exit_message():
    """Displays a graceful exit message."""
    print("\nOkay, you want to quit the bot.")
    time.sleep(1)
    print("At your command...!")
    time.sleep(1)
    print("Checking the bot for shutdown...")
    time.sleep(2)
    print("Initiating the abort process...!")
    time.sleep(3)
    print("\n" + "="*40)
    print("    THANK YOU FOR YOUR TIME SIR....!")
    print("    ANYTIME AT YOUR SERVICE...||")
    print("    SAY WHEN YOU ARE READY...!!!!!")
    print("="*40 + "\n")

def initialize_chat_model():
    """Initializes and returns the AzureChatOpenAI model."""
    try:
        model = AzureChatOpenAI(
            api_version=AZURE_OPENAI_API_VERSION,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME, # Use azure_deployment for deployment name
            model=MODEL_NAME
        )
        return model
    except Exception as e:
        print(f"Error initializing OpenAI model: {e}")
        print("Please check your environment variables and network connection.")
        return None

# --- Main Chat Function ---

def chat_bot():
    """Main function to run the interactive chat bot."""

    model = initialize_chat_model()
    if not model:
        return # Exit if model initialization failed

    # LangChain recommends storing chat history as a list of messages
    messages = []

    print("--- Welcome to the Azure OpenAI Chat Bot ---")
    while True:
        access_choice = input("Type 'CHAT' to enter or 'EXIT' to quit: ").lower().strip()

        if access_choice == 'exit':
            display_exit_message()
            break  # Exit the loop and end the program
        elif access_choice == 'chat':
            print("\nHELLO SIR.....!")
            time.sleep(1)
            print("Checking the bot to initiate....!")
            time.sleep(2)
            print("It is working fine. Let's start chatting!")
            print("-" * 30)

            while True:
                user_prompt = input("Ask anything you want or type 'EXIT' to quit: ").strip()

                if user_prompt.lower() == 'exit':
                    display_exit_message()
                    return # Exit the function, ending the program
                elif not user_prompt:
                    print("Please enter a question or 'EXIT' to quit.")
                    continue

                # Add user message to history
                messages.append(HumanMessage(content=user_prompt))

                try:
                    # Invoke the model with the current messages for context
                    response = model.invoke(messages)
                    print("\nBot:", response.content)
                    # Add AI message to history
                    messages.append(AIMessage(content=response.content))
                except Exception as e:
                    print(f"An error occurred during chat: {e}")
                    print("Please try again or check your internet connection.")
                    # Optionally, you might want to remove the last human message from history
                    # if the API call failed, to avoid confusing the model.
                    if messages and isinstance(messages[-1], HumanMessage):
                        messages.pop()

        else:
            print("Invalid input. Please type 'CHAT' or 'EXIT'.")

# --- Run the bot ---
if __name__ == "__main__":
    chat_bot()