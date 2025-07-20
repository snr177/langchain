from langchain_openai import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import streamlit as st  # type: ignore # Streamlit type definitions
from pydantic import SecretStr
import os
import time
import random
from typing import Optional, List, Dict, Any

# Set page title and configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="💬",
    layout="wide"
)

# Custom CSS to make the app look more like ChatGPT
st.markdown("""
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.assistant {
        background-color: #475063;
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .avatar img {
        max-width: 48px;
        max-height: 48px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message .message {
        width: 80%;
        padding-left: 1.5rem;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    .stTextInput > div > div > input {
        background-color: #2b313e;
        color: white;
    }
    .stTextArea > div > div > textarea {
        background-color: #2b313e;
        color: white;
    }
    .css-1oe6wy4, .css-1p0bytv, .css-12oz5g7 {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    header {
        background-color: #111827;
        height: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Add a title
st.title("Chat with AI Assistant")

# Sidebar with options
with st.sidebar:
    st.title("Settings")
    
    # Add temperature slider
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.temperature,
        step=0.1,
        help="Higher values make the output more random, lower values make it more deterministic"
    )
    st.session_state.temperature = temperature
    
    # Add a button to clear chat history
    if st.button("New Chat"):
        st.session_state.messages = []
        st.rerun()
    
    # Add info about the app
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This chat application uses Azure OpenAI to generate responses.
    Your conversation history is stored in the session and will be cleared when you refresh the page or start a new chat.
    """)
    st.markdown("---")
    
    # Add a download button for the chat history
    if st.session_state.get("messages") and len(st.session_state.messages) > 0:
        chat_text = "\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.download_button(
            label="Download Chat",
            data=chat_text,
            file_name=f"chat_history_{time.strftime('%Y%m%d-%H%M%S')}.txt",
            mime="text/plain",
        )

# Load environment variables from .env file
load_dotenv()

# Initialize model
azure_endpoint: Optional[str] = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name: Optional[str] = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME") 
api_version: Optional[str] = os.getenv("AZURE_OPENAI_API_VERSION")
api_key: Optional[str] = os.getenv("AZURE_OPENAI_API_KEY")

# Check if all environment variables are available
if not all([azure_endpoint, deployment_name, api_version, api_key]):
    st.error("Missing required environment variables. Please check your .env file.")
    missing_vars = []
    if not azure_endpoint: missing_vars.append("AZURE_OPENAI_ENDPOINT")
    if not deployment_name: missing_vars.append("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not api_version: missing_vars.append("AZURE_OPENAI_API_VERSION")
    if not api_key: missing_vars.append("AZURE_OPENAI_API_KEY")
    st.warning(f"Missing variables: {', '.join(missing_vars)}")
    st.stop()

# Initialize session state for storing conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today?"}
    ]

# Function to display chat messages
def display_chat_message(role, content, avatar=None):
    """Display a chat message with the given role and content."""
    if role == "user":
        avatar_img = "👤"
        message_alignment = "user"
    else:
        avatar_img = "🤖"
        message_alignment = "assistant"
        
    st.markdown(f"""
    <div class="chat-message {message_alignment}">
        <div class="avatar">
            <div>{avatar_img}</div>
        </div>
        <div class="message">{content}</div>
    </div>
    """, unsafe_allow_html=True)

# Initialize model
try:
    # At this point we've verified api_key is not None
    if api_key:  # This check helps type checking
        model = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_version=api_version,
            api_key=SecretStr(api_key),
            temperature=st.session_state.temperature,
        )
except Exception as e:
    st.error(f"Error initializing model: {str(e)}")
    st.stop()

# Display chat history
for message in st.session_state.messages:
    display_chat_message(message["role"], message["content"])

# Create a container for the chat input at the bottom of the page
with st.container():
    # Add some vertical space
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Create a two-column layout for input and button
    col1, col2 = st.columns([6, 1])
    
    with col1:
        # Clear the input if the flag is set
        if st.session_state.get("clear_input", False):
            st.session_state.user_input = ""
            st.session_state.clear_input = False
            
        user_input = st.text_input("", placeholder="Type your message here...", key="user_input", label_visibility="collapsed").upper()
    
    with col2:
        submit_button = st.button("Send")

# Initialize the input field clearing mechanism
if "clear_input" not in st.session_state:
    st.session_state.clear_input = False

# Callback to handle input clearing
def clear_input_callback():
    st.session_state.clear_input = True

# Process user input
if (submit_button or user_input) and user_input:
    current_input = user_input  # Store the current input
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": current_input})
    
    # Display the user message
    display_chat_message("user", current_input)
    
    # Generate response
    with st.spinner("Thinking..."):
        try:
            # Get response from the model
            response = model.invoke(current_input)
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.content})
            
            # Display the AI response
            display_chat_message("assistant", response.content)
            
            # Set flag to clear input on next rerun
            clear_input_callback()
            
            # Force a rerun to update the UI immediately
            st.rerun()
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")