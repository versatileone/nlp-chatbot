import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define simple patterns and responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm a bot, but I'm doing fine!",
    "your name": "I'm a simple chatbot.",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure, I'm here to help. Ask me anything.",
}

# Function to preprocess input
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

# Function to find response
def get_response(user_input):
    words = preprocess(user_input)
    for key in responses:
        key_words = preprocess(key)
        if set(key_words).intersection(words):
            return responses[key]
    return "Sorry, I don't understand that."

# Chat loop
def chat():
    print("SimpleBot: Hello! Type something or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("SimpleBot: Goodbye!")
            break
        print("SimpleBot:", get_response(user_input))

if __name__ == "__main__":
    chat()
