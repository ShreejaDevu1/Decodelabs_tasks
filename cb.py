print("AI Chatbot Started!")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I'm doing great!,what about you?")

    elif user == "what is your name":
        print("Bot: I'm Alex,your personalized AI chatbot.")

    elif user == "bye" or user == "exit":
        print("Bot: byeee!")
        break

    else:
        print("Bot: Sorry, I don't understand.")