import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import load_model
import random

# Load the pre-trained model and other necessary files
model = load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
intents = json.load(open(r'intents.json', encoding="utf-8"))
lemmatizer = WordNetLemmatizer()

def get_bot_response(user_input):
    # Clean up user input
    sentence_words = nltk.word_tokenize(user_input)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    
    # Generate bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    # Predict the intent class
    results = model.predict(np.array([bag]))[0]
    results_index = np.argmax(results)
    tag = classes[results_index]

    # Choose a random response from the intents JSON file
    for intent in intents['intents']:
        if intent['tag'] == tag:
            responses = intent['responses']
            response = random.choice(responses)
            break

    return response

# Conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        response = get_bot_response(user_input)
        print("Bot:", response)
