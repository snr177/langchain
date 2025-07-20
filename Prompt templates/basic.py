"""
LangChain Prompt Templates Example

This script demonstrates different ways to create and use prompt templates with LangChain,
including both basic templates and structured chat prompts with the ChatPromptTemplate class.
It shows how to format prompts, invoke a language model, and handle the responses.

Author: Your Name
Date: June 15, 2025
"""

import os
from typing import Dict, Any

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import AzureChatOpenAI


def load_model() -> AzureChatOpenAI:
    """
    Initialize and return an Azure OpenAI chat model using environment variables.
    
    Returns:
        AzureChatOpenAI: Configured language model client
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get configuration from environment variables
    endpoint = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    
    if not endpoint or not api_version:
        raise ValueError("Missing required environment variables for Azure OpenAI")
    
    # Initialize the model using the parameter names that work in your environment
    return AzureChatOpenAI(
        azure_deployment=endpoint,
        api_version= api_version,
        temperature=0.7,  # Controls randomness (0 = deterministic, 1 = creative)
    )


def simple_template_example(model: AzureChatOpenAI) -> None | str:
    """
    Demonstrate using a simple string template with ChatPromptTemplate.
    
    Args:
        model: The language model to use
    """
    print("\n==== SIMPLE TEMPLATE EXAMPLE ====")
    
    # Create a template with a variable {assistant}
    template = """I want you to act as {assistant}, the world's most helpful AI assistant.
Please respond to my questions in a knowledgeable, concise, and friendly manner.
If you don't know something, admit it rather than making up information."""
    
    # Create a prompt from the template
    prompt = ChatPromptTemplate.from_template(template=template)
    print("✓ Prompt template created")
    
    # Format the prompt with our variable
    formatted_prompt = prompt.invoke({"assistant": "JARVIS"})
    print("\n--- Formatted Prompt ---")
    print(formatted_prompt)
    
    # Call the model with our formatted prompt
    model_response = model.invoke(formatted_prompt)
    print("\n--- Model Response ---")
    print(f"Content: {model_response.content}")


def music_recommendation_example(model: AzureChatOpenAI) -> None | str:
    """
    Demonstrate using a structured chat prompt with system and user messages.
    
    Args:
        model: The language model to use
    """
    print("\n==== MUSIC RECOMMENDATION EXAMPLE ====")
    
    # Create structured messages for a music recommendation system
    messages = [
        {
            "role": "system",
            "content": """You are an expert music advisor with deep knowledge of all genres, artists, and songs.
Your expertise covers classical, jazz, rock, pop, electronic, hip-hop, R&B, country, folk, and world music.

Guidelines:
- Recommend 5 specific songs based on the user's mood, including artist names
- Briefly explain why each song matches their mood (1 sentence per song)
- Include a mix of well-known and lesser-known artists
- Add a short playlist name that captures the mood"""
        },
        {
            "role": "user",
            "content": "I'm feeling {mood} today. Can you suggest some music that would match my mood?"
        }
    ]
    
    # Create a prompt from the messages
    prompt = ChatPromptTemplate.from_messages(messages=messages)
    print("✓ Chat prompt template created")
    
    # Test with different moods
    moods = ["melancholy", "energetic", "relaxed", "focused"]
    respnse = input("Write your emotion to start testing with different moods...")
       
  
    if respnse.lower() in moods:
        print(f"\n--- Testing with mood: {respnse} ---")
        formatted_prompt = prompt.invoke({"mood": respnse})
        
        # Call the model with our formatted prompt
        try:
            model_response = model.invoke(formatted_prompt)
            print(f"Music recommendations for '{respnse}' mood:\n{model_response.content}")
        except Exception as e:
            print(f"Error getting response: {e}")
    else:
        print("it seems you have entered an mood is not in our list. ")
        print("Well that's okay, i am going to add the mood you entered to our list.")
        print(f"Adding '{respnse}' to our mood list for future reference.")
        # Add the new mood to the list
        moods.append(respnse)
        print(f"Updated mood list: {moods}")
        print(f"\n--- Testing with mood: {respnse} ---")
        formatted_prompt = prompt.invoke({"mood": respnse})
        try:
            model_response = model.invoke(formatted_prompt)
            print(f"Music recommendations for '{respnse}' mood:\n{model_response.content}")
        except Exception as e:
            print(f"Error getting response: {e}")

def main():
    """Main function to run all examples."""
    try:
        model = load_model()
        simple_template_example(model)
        music_recommendation_example(model)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()