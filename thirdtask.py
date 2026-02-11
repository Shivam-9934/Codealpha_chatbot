def chatbot():
    print("🤖 CHATBOT: Hello! I'm CodeAlpha Bot. Type 'bye' to exit.")
    
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! Nice to meet you!",
        "how are you": "I'm doing great, thanks for asking!",
        "what is your name": "I'm CodeAlpha Bot, your virtual assistant!",
        "what can you do": "I can chat with you and answer simple questions!",
        "who created you": "I was created by CodeAlpha for the Python internship program.",
        "python": "Python is awesome! It's simple, powerful, and great for beginners.",
        "help": "You can say hello, ask my name, or just chat with me!",
        "thanks": "You're welcome! Happy to help! 😊",
        "bye": "Goodbye! Have a great day!"
    }
    
    while True:
        user_input = input("\nYou: ").lower().strip()
        
        if not user_input:
            continue
            
        if user_input == 'bye':
            print("🤖 CHATBOT: Goodbye! See you next time!")
            break
            
        replied = False
        for pattern in responses:
            if pattern in user_input:
                print(f"🤖 CHATBOT: {responses[pattern]}")
                replied = True
                break
                
        if not replied:
            print("🤖 CHATBOT: I'm not sure how to respond to that. Try saying 'hello' or 'help'.")

if __name__ == "__main__":
    chatbot()