# Deploying to Streamlit Cloud

This directory contains a Streamlit application that can be deployed to Streamlit Cloud. Follow these steps to deploy the application.

## Files Overview

- `practice_session_app.py`: The main application code organized as a module
- `streamlit_app.py`: Entry point for Streamlit Cloud
- `2_prac.py`: The original application file (backup)
- `requirements.txt`: Dependencies required for the application
- `.streamlit/config.toml`: Streamlit configuration for theming

## How to Deploy

### Step 1: Connect to Streamlit Cloud

1. Create an account at [Streamlit Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository

### Step 2: Configure the Deployment

1. Select this repository
2. Set the main file path to `practice session/streamlit_app.py`
3. Add the required secrets (see below)

### Step 3: Add Environment Variables

Add the following secrets in the Streamlit Cloud dashboard:

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_DEPLOYMENT_NAME`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_API_KEY`

## Local Development

To run the application locally:

```bash
streamlit run practice_session_app.py
```

Make sure you have a `.env` file in this directory with the required environment variables.
