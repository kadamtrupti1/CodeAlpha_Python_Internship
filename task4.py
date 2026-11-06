
# CodeAlpha Python Programming Internship
# Task 4: Basic Chatbot

# STEP 1: Create a function for the chatbot.
# A function is a block of code that performs a particular task.

def chatbot():

    # Display the chatbot's welcome message.

    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)

    print("Bot: Hello! I am your friendly chatbot.")
    print("Bot: You can talk to me. Type 'bye' to exit.")

    # STEP 2: Start an infinite loop.
    # This allows the user to send multiple messages.
    # The loop will stop when the user types 'bye'.

    while True:

        # Take a message from the user.
        # lower() converts the message into lowercase.
        # strip() removes unnecessary spaces.

        user_input = input("\nYou: ").lower().strip()

        # STEP 3: Check the user's message.
        # if-elif conditions select the appropriate reply.

        if user_input == "hello" or user_input == "hi":

            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":

            print("Bot: I'm fine, thanks! How about you?")

        elif user_input == "what is your name":

            print("Bot: I'm Python Bot, your friendly chatbot!")

        elif user_input == "what can you do":

            print("Bot: I can chat with you using predefined replies.")

        elif user_input == "thank you" or user_input == "thanks":

            print("Bot: You're welcome!")

        elif user_input == "bye":

            print("Bot: Goodbye! Have a great day!")

            # break stops the loop and ends the conversation.

            break

        # If the message does not match any condition,
        # the chatbot displays a default response.

        else:

            print("Bot: Sorry, I don't understand that message.")

# STEP 4: Call the function to start the chatbot.

chatbot()
