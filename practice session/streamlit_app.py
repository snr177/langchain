import os
import sys

# Add this to detect if we're running on Streamlit Cloud
os.environ["STREAMLIT_SHARING_MODE"] = "streamlit_cloud"

# Run the actual app
import streamlit as st
from dotenv import load_dotenv

# Load local .env file if present (for local development)
load_dotenv()

# Print import details for debugging
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Working directory:", os.getcwd())

# Use the main function from practice_session_app.py
try:
    from practice_session_app import main
    print("Successfully imported main function from practice_session_app")
except ImportError as e:
    print(f"Error importing practice_session_app: {e}")
    # Fall back to the 2_prac.py file if needed
    print("Falling back to 2_prac.py")
    # Execute the file directly
    exec(open("2_prac.py").read())
    sys.exit(0)

if __name__ == "__main__":
    main()
