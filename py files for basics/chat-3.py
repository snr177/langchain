from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os,time
load_dotenv()
model = init_chat_model("gemini-2.0-flash-lite", model_provider= "google_genai")
result = model.invoke("hi there..! i'm tony stark")
print(result.content)