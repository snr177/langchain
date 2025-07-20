import os
import sys

# Print diagnostic information to help with debugging
print("Streamlit App Startup - Diagnostic Information")
print("-" * 50)
print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")
print(f"Available files: {os.listdir('.')}")
print("-" * 50)

# Add this to detect if we're running on Streamlit Cloud
os.environ["STREAMLIT_SHARING_MODE"] = "streamlit_cloud"

# Try to import required packages and log any issues
try:
    import streamlit as st
    print("✅ Successfully imported streamlit")
except ImportError as e:
    print(f"❌ Error importing streamlit: {e}")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    print("✅ Successfully imported python-dotenv")
    # Load local .env file if present (for local development)
    load_dotenv()
except ImportError as e:
    print(f"❌ Error importing dotenv: {e}")
    # We can continue without dotenv on Streamlit Cloud

try:
    from langchain_openai import AzureChatOpenAI
    print("✅ Successfully imported langchain_openai")
except ImportError as e:
    print(f"❌ Error importing langchain_openai: {e}")
    st.error(f"Failed to import langchain_openai: {e}")
    st.stop()

# Use the main function from practice_session_app.py
try:
    from practice_session_app import main
    print("✅ Successfully imported main function from practice_session_app")
except ImportError as e:
    print(f"❌ Error importing practice_session_app: {e}")
    
    # Try to import fallback files in order of preference
    try:
        print("Attempting to use minimal_app.py as fallback...")
        if os.path.exists("minimal_app.py"):
            print("Found minimal_app.py, executing directly")
            st.title("Chat with AI Assistant (Minimal Mode)")
            st.info("Running in compatibility mode with simplified features.")
            exec(open("minimal_app.py").read())
            sys.exit(0)
        elif os.path.exists("2_prac.py"):
            print("Found 2_prac.py, executing directly")
            st.title("Chat with AI Assistant (Direct Mode)")
            st.warning("Running in compatibility mode. Some features may be limited.")
            exec(open("2_prac.py").read())
            sys.exit(0)
        else:
            print("❌ Could not find any fallback app")
            st.error("Could not load application. Please check logs for more information.")
            st.stop()
    except Exception as e2:
        print(f"❌ Error with fallback: {e2}")
        st.error(f"Application startup failed: {e2}")
        st.stop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error running main: {e}")
        st.error(f"An error occurred while running the application: {str(e)}")
        st.code(f"Error details: {e}")
        import traceback
        st.code(traceback.format_exc())
