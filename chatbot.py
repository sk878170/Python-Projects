import random

# Define responses for different types of user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm great, thanks for asking.", "All good, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."]
}

def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    
    # Check if user input matches any predefined responses
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit loop if user says "bye"
        if user_input.lower() == "bye":
            print("Chatbot:", get_response("bye"))
            break
        
        # Get chatbot response
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
