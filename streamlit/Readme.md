# Streamlit Applications for LangChain

This directory houses Streamlit applications that provide interactive web interfaces for LangChain functionalities, primarily focusing on chatbot implementations.

## Files

-   **`__init__.py`**: An empty file that marks this directory as a Python package, allowing for modular imports if needed.
-   **`chatbot.py`**: Contains the core logic for the Streamlit chatbot. This might include functions for handling user input, interacting with the LangChain backend (LLMs, chains, memory), and formatting the chat display. (Placeholder: Add more specific details about its responsibilities, e.g., "Manages session state for chat history, calls the LangChain model, and renders messages.")
-   **`main.py`**: The main entry point for the Streamlit application. This script typically sets up the Streamlit page configuration, initializes the chatbot components from `chatbot.py`, and defines the overall UI layout and user interaction flow. (Placeholder: Add more specific details, e.g., "Sets page title, sidebar elements, and orchestrates the chat interface.")

## Purpose

The primary goal of these files is to create user-friendly web applications for demonstrating and interacting with LangChain-powered models. This allows for easier testing, showcasing, and use of the underlying AI capabilities without needing to run command-line scripts.

## How to Use

1.  Ensure you have all dependencies installed from the main `requirements.txt` in the root of the `langchain` project. This includes Streamlit and any LangChain-related packages.
2.  Set up your environment variables (e.g., for Azure OpenAI or other LLM providers) as described in the main project `Readme.md` located at `e:\python\langchain\Readme.md`.
3.  Navigate to the root directory of the project (`e:\python\langchain`) in your terminal.
4.  Run the main Streamlit application using the following command:
    ```powershell
    streamlit run streamlit/main.py
    ```
5.  This command will start a local web server, and the application should automatically open in your default web browser. If not, the terminal will provide a URL (usually `http://localhost:8501`) that you can open manually.

## Customization

-   Modify `chatbot.py` to change the chatbot's behavior, such as the LLM used, prompt engineering, or memory management.
-   Adjust `main.py` to alter the user interface, add new Streamlit components, or change the application's layout.

Feel free to expand and enhance these Streamlit applications as you explore more LangChain features!
