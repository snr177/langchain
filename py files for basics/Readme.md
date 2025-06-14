# Python Scripts for LangChain Basics

This directory contains a collection of Python scripts and Jupyter Notebooks designed to explore the fundamental concepts of the LangChain library. Each file focuses on specific aspects, building up from simple examples to more complex interactions with language models.

## Scripts

-   **`chat-1.py`**: Basic LLM interaction example.
-   **`chat-2.py`**: Introduction to ChatModels and message types.
-   **`chat-3.py`**: Working with Prompt Templates.
-   **`chat-4.py`**: Implementing simple chains and workflows.
-   **`chat-5.py`**: Command-line chatbot using Azure OpenAI, demonstrating chat history and system messages.
-   **`grok.py`**: Utility and experimentation scripts for LangChain features.
-   **`firebase-2.py`**: Entry point for the Firestore-backed Azure OpenAI chatbot (see below for details).

## Notebooks

-   **`notebooks/notebook-1.ipynb`**: Interactive experiments with LangChain features, data loading, and retrieval-augmented generation (RAG).

## Purpose

The primary goal of these files is to provide hands-on examples for learning LangChain. They are intended to be run individually to understand specific functionalities.

## How to Use

1.  Ensure you have all dependencies installed from the main `requirements.txt` in the root of the `langchain` project.
2.  Set up your environment variables (e.g., for Azure OpenAI) as described in the main project `Readme.md`.
3.  Navigate to this directory (`py files for basics`) in your terminal.
4.  Run the Python scripts directly:
    ```powershell
    python chat-1.py
    python chat-5.py
    python firebase-2.py
    ```
5.  For the Jupyter Notebook, start a Jupyter server and open `notebooks/notebook-1.ipynb`.

Feel free to modify and experiment with these scripts as you learn!

---

# Firestore-Backed Azure OpenAI Chatbot (`firebase-2.py`)

This script demonstrates how to build a command-line chatbot using Azure OpenAI for conversational AI and Google Firestore for persistent chat history storage. The code is modular, user-friendly, and well-commented for easy understanding and extension.

## Features

- **Interactive CLI Chatbot:** Chat with an AI assistant directly from your terminal.
- **Persistent Chat History:** All messages are stored and retrieved from Google Firestore.
- **Azure OpenAI Integration:** Uses Azure OpenAI for generating AI responses.
- **ASCII Art Welcome:** Displays a fun ASCII art banner at startup (optional).
- **User-Friendly Prompts:** Clear instructions and graceful exit handling.

## Requirements

- Python 3.8+
- Google Cloud Firestore credentials (set up via environment variables)
- Azure OpenAI API access
- Required Python packages (see below)

## Installation

1. **Clone the repository**
   ```powershell
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root with the following keys:
   ```env
   AZURE_OPENAI_DEPLOYMENT_NAME=your_azure_deployment_name
   AZURE_OPENAI_API_VERSION=your_azure_api_version
   PROJECT_ID=your_firestore_project_id
   SESSION_ID=your_unique_session_id
   COLLECTION_NAME=your_firestore_collection_name
   ```
   Also ensure your Google Cloud credentials are set up for Firestore access.

4. **(Optional) Add ASCII Art**
   Place a text file named `ascii-text-art.txt` in the project root for a custom welcome banner.

## Usage

Run the script from the terminal:
```powershell
python firebase-2.py
```

You will be prompted to choose an action:
- `chat` — Start chatting with the AI assistant.
- `history` — View your chat history from Firestore.
- `exit` — Exit the chatbot gracefully.

## Code Structure

- **Environment Setup:** Loads environment variables and initializes Azure OpenAI and Firestore clients.
- **instructions() Function:** Contains the main chatbot loop, user prompts, and logic for chat, history, and exit actions.
- **ASCII Art Display:** Shows a banner if `ascii-text-art.txt` is present.
- **Error Handling:** Handles missing files, invalid input, and API errors gracefully.

## Example Session

```
Choose an action ('chat', 'history', 'exit'): chat
OKAY, CONTINUE TO CHAT..!
Initializing...
All set!
Ready...

ENTER YOUR QUERY: Hello, AI!
AI: Hello! How can I assist you today?

Choose an action ('chat', 'history', 'exit'): history
PLEASE WAIT...!
PAST MESSAGES:
[...chat history from Firestore...]

Choose an action ('chat', 'history', 'exit'): exit
PLEASE WAIT...!
ABORTING
Exiting the bot
EXITED
THANK YOU FOR YOUR TIME...!
```

## Customization

- **Change the AI Model:** Modify the `AzureChatOpenAI` initialization as needed.
- **Change Firestore Collection:** Update the `COLLECTION_NAME` in your `.env` file.
- **Add More Actions:** Extend the `instructions()` function for more features.

## Troubleshooting

- Ensure all required environment variables are set. The script will fail if any are missing.
- Make sure your Google Cloud credentials are configured for Firestore access.
- If you see errors about missing files, check that `ascii-text-art.txt` exists (or ignore if you don't want a banner).

## License

This project is open-source and available under the MIT License.

---

*Happy chatting!*
