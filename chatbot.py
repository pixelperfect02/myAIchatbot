import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request, jsonify

# Download necessary data (only once)
nltk.download('punkt')
nltk.download('stopwords')

# Define patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello, how can I assist you?", "Hi there! How can I help?"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
    (r"(.*) your name?", ["I'm just a simple chatbot!", "I'm a bot created to assist you."]),
    (r"(.*) (help|assist) (.*)", ["Sure! How can I assist you?", "What do you need help with?"]),
    (r"(.*) (location|from)", ["I am based in the cloud, ready to assist you anytime!"]),
    (r"what (.*) you do", ["I can answer questions, assist with tasks, and chat with you!"]),
    (r"bye|exit|quit", ["Goodbye! Have a great day!", "Take care!"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Can you clarify?"]),
]

# Create the chatbot instance
chat = Chat(pairs, reflections)

# Function to get a response based on user input
def get_response(user_input):
    return chat.respond(user_input)  # Get the response from the Chat object

# Initialize Flask app
app = Flask(__name__)

# Route to render the homepage (frontend)
@app.route('/')
def home():
    return render_template('index.html')  # Make sure this template exists!

# Route to handle chatbot messages (AJAX)
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']  # Get the message from the frontend
    bot_response = get_response(user_input)  # Get the chatbot's response from the get_response function
    return jsonify({'response': bot_response})  # Send the response back to frontend

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)


# import nltk
# from flask import Flask, render_template, request, jsonify
# from transformers import pipeline

# # Initialize Hugging Face's GPT-2 model (or other models like GPT-3, depending on your setup)
# chatbot = pipeline('text-generation', model='gpt2')

# # Initialize Flask app
# app = Flask(__name__)

# # Route to render the homepage (frontend)
# @app.route('/')
# def home():
#     return render_template('index.html')  # Make sure this template exists!

# # Route to handle chatbot messages (AJAX)
# @app.route('/ask', methods=['POST'])
# def ask():
#     user_input = request.form['message']  # Get the message from the frontend
#     bot_response = get_response(user_input)  # Get the AI-generated response
#     return jsonify({'response': bot_response})  # Send the response back to frontend

# # Function to get the response from GPT-2
# def get_response(user_input):
#     response = chatbot(user_input, max_length=50, num_return_sequences=1)
#     return response[0]['generated_text']

# # Start the Flask server
# if __name__ == "__main__":
#     app.run(debug=True)
