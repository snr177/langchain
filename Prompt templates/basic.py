from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

# Example using a template
# template = "I want you to act as the best AI assistant in the world like {assistant}"
# prompt = ChatPromptTemplate.from_template(template=template)
# print("--------prompt from template---------")
# prompt_thing = prompt.invoke({"assistant": "jarvis"})
# print(prompt_thing)

# Correct message format for ChatPromptTemplate
messages = [
    {"role": "system",
      "content": "You are a great versatile musician who can play based on mood so give suggest me some music and songs."},
    {"role": "user",
      "content": "Suggest me some music based on my mood {mood}."}
]
prompt = ChatPromptTemplate.from_messages(messages=messages)
print("--------prompt from messages---------")
prompt_thing = prompt.invoke({"mood": "happy"})
print(prompt_thing)