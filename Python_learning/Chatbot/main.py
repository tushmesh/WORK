import nltk
import numpy as np
import random
import string

# Importing the NLTK modules
from nltk.chat.util import Chat, reflections

# Preprocessing
nltk.download('punkt')
nltk.download('wordnet')

# Defining responses
responses = [
    (r"hi", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you", ["I'm good, thank you!", "Feeling great, thanks!", "I'm doing well."]),
    (r"what's your name?", ["I'm just a chatbot!", "I don't have a name, I'm just a program."]),
    (r"bye", ["Goodbye!", "Bye!", "See you later!"]),
    (r".*", ["I'm not sure I understand.", "Could you please rephrase that?", "I'm just a simple chatbot."])
]

# Defining the chatbot
def chatbot():
    print("Welcome! Ask me anything or say 'bye' to exit.")
    chat = Chat(responses, reflections)
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print(random.choice(responses[-1][1]))  # Saying goodbye randomly from the default responses
            break
        else:
            print("Chatbot:", chat.respond(user_input))

# Running the chatbot
if __name__ == "__main__":
    chatbot()
