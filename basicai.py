def chatbot():
    responses = {
        "hello": "Hello! Do you have any questions?",
        "where are you from": "I'm a chatbot and I don't exist in a physical location.",
        "favorite food": "I'm a chatbot, so I don't have the ability to eat, but people generally like foods such as pizza and chicken dishes.",
        "favorite color": "I'm a chatbot, so I can't perceive colors, but people usually like colors such as blue, green, and red."
    }

    print("Hello, how can I assist you?")
    while True:
        user_input = input("What question would you like to ask? (Type 'exit' to quit) ")
        if user_input.lower() in responses:
            print(responses[user_input.lower()])
        elif user_input.lower() == "exit":
            print("Goodbye, see you again!")
            break
        else:
            print("Sorry, I didn't understand. Let's try a different question.")

chatbot()
