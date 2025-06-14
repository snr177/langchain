# LangChain Learning Repository

Welcome! This repository documents practical learning and experimentation with [LangChain](https://python.langchain.com/), OpenAI, and related tools. It includes scripts, notebooks, and web apps for building and exploring language model applications.

## Project Structure

```
.
├── LICENSE
├── Readme.md
├── requirements.txt
├── chatwithyourdata/       # Data-centric experiments and PDF/web loaders
├── py files for basics/    # Core Python scripts and notebooks for LangChain
│   ├── chat-1.py           # Basic LLM interaction
│   ├── chat-2.py           # ChatModels and message types
│   ├── chat-3.py           # Prompt Templates
│   ├── chat-4.py           # Simple chains and workflows
│   ├── chat-5.py           # CLI chatbot with Azure OpenAI
│   ├── grok.py             # Utility/experimentation scripts
│   ├── firebase-2.py       # Firestore-backed Azure OpenAI chatbot
│   └── notebooks/
│       └── notebook-1.ipynb # Jupyter notebook for interactive experiments
└── streamlit/              # Streamlit web applications
    ├── __init__.py
    ├── chatbot.py          # Chatbot logic for Streamlit
    └── main.py             # Main Streamlit app
```

## Getting Started

1. **Clone the repository:**
    ```powershell
    git clone <your-repository-url>
    cd langchain
    ```
2. **(Recommended) Create and activate a virtual environment:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
3. **Install dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```
4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys and configuration details. Example:
    ```env
    AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
    AZURE_OPENAI_API_VERSION=your_api_version
    AZURE_OPENAI_API_KEY=your_api_key
    # Add other necessary environment variables
    ```

## Usage

- **Run a Python script:**
    ```powershell
    cd "py files for basics"
    python chat-5.py
    python firebase-2.py
    ```
- **Run the Streamlit app:**
    ```powershell
    streamlit run streamlit/main.py
    ```
- **Open a notebook:**
    Open `notebooks/notebook-1.ipynb` in Jupyter or VS Code.

## Screenshots & Demos

Add screenshots or GIFs of your applications in an `images/` folder for better documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)

---

*Happy building and learning!*