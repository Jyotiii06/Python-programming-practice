def chatbot():
    print("Hello! I am a simple AI chatbot. Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user=="hi" or user=="Hi" or user=="Hy" or user=="hy":
            print("Bot: Hi there!")
        elif user == "how are you":
            print("Bot: I'm just code, but I'm doing great!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that yet.")

chatbot()
