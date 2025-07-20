"""
Minimal Streamlit app for chat with Azure OpenAI
"""
import streamlit as st
import os
from dotenv import load_dotenv
from pydantic import SecretStr

# Helper function to safely convert string to SecretStr
def safe_secret(value):
    if value is None:
        return None
    try:
        return SecretStr(value)
    except Exception:
        # If there's any issue with SecretStr, return the string value
        # This ensures compatibility with different pydantic versions
        return value

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="AI Chat", page_icon="💬")

# Add title
st.title("AI Chat Assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today?"}
    ]

# Sidebar
with st.sidebar:
    st.title("Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    
    # New chat button
    if st.button("New Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today?"}
        ]
        st.rerun()

# Get API credentials
azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
api_key = os.environ.get("AZURE_OPENAI_API_KEY")

# Check for credentials
if not all([azure_endpoint, deployment_name, api_version, api_key]):
    st.error("Missing API credentials")
    st.stop()

# Initialize OpenAI client
try:
    from langchain_openai import AzureChatOpenAI
    
    # First try with SecretStr
    try:
        model = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_version=api_version,
            api_key=safe_secret(api_key),  # Try with our safe_secret helper first
            temperature=temperature,
        )
    except Exception as e:
        st.warning(f"First initialization attempt failed: {str(e)}")
        # Fall back to direct string usage if SecretStr fails
        model = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_version=api_version,
            api_key=api_key,  # Use string directly as fallback
            temperature=temperature,
        )
except Exception as e:
    st.error(f"Error initializing model: {str(e)}")
    st.stop()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Type your message here...")

# Process user input
if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(user_input)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
                st.write(response.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
