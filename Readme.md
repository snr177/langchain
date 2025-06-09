# LangChain Learning Journey 🚀

<!-- Optional: Add a logo or a relevant banner image here -->
<!-- ![LangChain Logo](images/langchain-logo.png) -->

---

Welcome to my LangChain learning repository! This project documents my journey of learning and building applications using [LangChain](https://python.langchain.com/), OpenAI, and related technologies. Here, I'm turning mistakes into milestones and exploring the capabilities of large language models.

---

## 📚 Project Structure

The repository is organized as follows:

```
.
├── LICENSE
├── Readme.md
├── requirements.txt
├── chatwithyourdata/       # (Placeholder: Add description if this folder is in use)
├── py files for basics/    # Core Python scripts for LangChain fundamentals
│   ├── chat-1.py
│   ├── chat-2.py
│   ├── chat-3.py
│   ├── chat-4.py
│   ├── chat-5.py           # CLI chat application with Azure OpenAI
│   ├── grok.py             # (Placeholder: Add description for grok.py)
│   └── notebooks/
│       └── notebook-1.ipynb # Jupyter notebook for experiments
└── streamlit/              # Streamlit applications
    ├── __init__.py
    ├── chatbot.py          # Core chatbot logic for Streamlit
    └── main.py             # Main Streamlit application file
```

---

## 🏗️ What’s Inside

- **`py files for basics/`**: Contains foundational Python scripts that demonstrate various LangChain concepts, from basic chains to more complex agent implementations and chat history management.
- **`py files for basics/notebooks/`**: Jupyter Notebooks for interactive coding sessions, experimentation, and visualizing outputs.
- **`streamlit/`**: Houses Streamlit applications that provide a web-based UI for interacting with the LangChain models. This includes a chatbot interface.
- **`chatwithyourdata/`**: *(Please provide a description for this folder if it's actively used, e.g., "Scripts and resources for building chatbots that can interact with your custom data sources.")*

---

## 🚦 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Git

### Installation

1.  **Clone the repository:**
    ```powershell
    git clone <your-repository-url>
    cd langchain
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory (`e:\python\langchain\.env`) and add your API keys and configuration details. For example:
    ```env
    AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"
    AZURE_OPENAI_API_KEY="your_api_key"
    # Add other necessary environment variables
    ```
    *Note: The `chat-5.py` script specifically uses these Azure OpenAI environment variables.*

### Running the Applications

-   **Basic Python Scripts:**
    Navigate to the `py files for basics` directory and run any of the Python scripts:
    ```powershell
    cd "py files for basics"
    python chat-5.py
    ```

-   **Streamlit Chatbot:**
    Navigate to the root directory and run the Streamlit application:
    ```powershell
    streamlit run streamlit/main.py
    ```
    This will typically open the application in your default web browser.

---

## 🖼️ Screenshots & Demos

*(It's highly recommended to add screenshots of your applications or a GIF demonstrating their functionality. Create an `images` folder in your repository to store them.)*

**Example: CLI Chat in Action**
<!-- ![CLI Chat Example](images/cli-chat-example.png) -->
*Caption: A screenshot of the `chat-5.py` command-line interface.*

**Example: Streamlit Web Application**
<!-- ![Streamlit Chatbot UI](images/streamlit-chatbot-ui.png) -->
*Caption: The user interface of the Streamlit chatbot.*

---

## 📅 Learning Log & Progress

*(This section can be updated regularly to reflect your learning progress.)*

-   **Week 1 (Starting June 3, 2025 - June 9, 2025):**
    -   Set up the project structure.
    -   Explored basic LangChain concepts: LLMs, ChatModels, Prompt Templates.
    -   Implemented a simple command-line chat application (`chat-5.py`) with memory.
    -   Started development of a Streamlit-based chatbot interface.
    -   Initial `Readme.md` creation.

*(Add more weeks and details as you progress.)*

---

## 🎯 Goals & Future Plans

-   [ ] Explore different types of chains and agents in LangChain.
-   [ ] Integrate custom data sources for Q&A.
-   [ ] Experiment with different LLMs.
-   [ ] Enhance the Streamlit application with more features.
-   [ ] Document learnings and challenges encountered.

---

## 🤝 Contributing

While this is primarily a personal learning project, suggestions, feedback, and contributions are welcome! Please feel free to:
-   Open an issue to report bugs or suggest features.
-   Fork the repository and submit a pull request with your enhancements.

---

## 📜 License

This project is licensed under the terms of the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

-   The [LangChain Team](https://www.langchain.com/) for the amazing framework.
-   [OpenAI](https://openai.com/) for their powerful language models.
-   [Streamlit](https://streamlit.io/) for making web app development in Python so accessible.

---

*Happy Learning!*