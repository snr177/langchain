# AI Chat Assistant

This is a Streamlit application that uses Azure OpenAI to create a ChatGPT-like interface.

## Features

- Chat with an AI assistant powered by Azure OpenAI
- Adjust temperature to control response randomness
- Save conversation history
- Modern, responsive UI similar to ChatGPT

## Deployment Instructions

### Local Development

1. Clone this repository
2. Create a `.env` file with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_ENDPOINT=your_endpoint_here
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name_here
   AZURE_OPENAI_API_VERSION=your_api_version_here
   AZURE_OPENAI_API_KEY=your_api_key_here
   ```
3. Install requirements: `pip install -r requirements.txt`
4. Run the app: `streamlit run 2_prac.py`

### Streamlit Cloud Deployment

1. Connect your GitHub repository to Streamlit Cloud
2. Set the main file path to `practice session/2_prac.py`
3. Add the following secrets in the Streamlit Cloud dashboard:
   - AZURE_OPENAI_ENDPOINT
   - AZURE_OPENAI_DEPLOYMENT_NAME
   - AZURE_OPENAI_API_VERSION
   - AZURE_OPENAI_API_KEY
4. Deploy!

## Note

This application requires valid Azure OpenAI credentials. If you don't have them, you'll need to sign up for Azure OpenAI service.
