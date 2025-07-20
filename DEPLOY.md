# Azure OpenAI Streamlit Chat App

A simple Streamlit chat application that uses Azure OpenAI API through the LangChain framework.

## Features

- ChatGPT-like interface with chat bubbles
- Conversation history management
- Configurable temperature setting
- New chat functionality
- Error handling for API issues

## Setup Instructions

### Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   For minimal installation:
   ```
   pip install -r requirements-minimal.txt
   ```

4. Create a `.env` file with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OPENAI_API_VERSION=your_api_version
   AZURE_OPENAI_API_KEY=your_api_key
   ```

5. Run the application:
   ```
   streamlit run streamlit_app.py
   ```

### Streamlit Cloud Deployment

1. Push your code to a GitHub repository
2. Create a new app on [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository and set the main file to `streamlit_app.py`
4. Add your Azure OpenAI credentials as secrets in the Streamlit Cloud dashboard
5. Deploy the app

## Deployment Troubleshooting

If you encounter issues with the deployment, try the following:

1. Use the minimal requirements file:
   ```
   pip install -r requirements-minimal.txt
   ```

2. Ensure your environment variables are correctly set in Streamlit Cloud's secrets management

3. Check the Streamlit Cloud logs for any specific error messages

## Files

- `streamlit_app.py`: Main application file for deployment
- `practice_session/practice_session_app.py`: Full-featured application
- `practice_session/minimal_app.py`: Minimal version of the application for fallback

## Dependencies

- streamlit
- langchain
- langchain-openai
- python-dotenv
- pydantic
