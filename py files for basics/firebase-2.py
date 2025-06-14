"""
Entry point for the Firestore-backed Azure OpenAI CLI chatbot.
Displays optional ASCII art, prints instructions, and launches the chatbot.
"""
import os
from instruct import instructions

def display_ascii_art(filename="ascii-text-art.txt"):
    """
    Display ASCII art from a file if it exists.
    """
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("ASCII art file not found. Continuing without it.")

if __name__ == "__main__":
    # Display ASCII art at startup (optional)
    display_ascii_art()
    # Show function docstring and start the chatbot
    if callable(instructions):
        print(instructions.__doc__)
        instructions()
    else:
        print("Error: 'instructions' function not found in instruct module.")
