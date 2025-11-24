# ==========================================
# CODSOFT - TASK 1: Advanced Rule-Based Chatbot
# Features:
# - Greetings
# - Personal queries
# - Date & time
# - Small talk
# - Simple math solving
# - FAQ style responses
# - Modular rule system
# ==========================================

import re
import datetime

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")


def solve_math(expression):
    try:
        return str(eval(expression))
    except:
        return "Sorry, I couldn't solve that."


def respond(user_input):
    text = user_input.lower()

    # -----------------------------------------------
    # 1. Greetings
    # -----------------------------------------------
    if re.search(r"\b(hi|hello|hey|hola|namaste)\b", text):
        return "Hi there! 😊 How can I assist you today?"

    # -----------------------------------------------
    # 2. Asking about chatbot
    # -----------------------------------------------
    elif re.search(r"who are you|what are you|your name", text):
        return "I'm an AI chatbot designed to help you with basic tasks and conversations!"

    # -----------------------------------------------
    # 3. Date and Time
    # -----------------------------------------------
    elif "time" in text:
        return f"The current time is {get_time()}."

    elif "date" in text:
        return f"Today's date is {get_date()}."

    # -----------------------------------------------
    # 4. Simple Math
    # User says: "solve 23+14", "what is 40/5", "calculate 5*9"
    # -----------------------------------------------
    match = re.search(r"solve (.*)|calculate (.*)|what is (.*)", text)
    if match:
        expression = match.group(1) or match.group(2) or match.group(3)
        return f"The answer is {solve_math(expression)}."

    # -----------------------------------------------
    # 5. Emotional Conversation
    # -----------------------------------------------
    elif "how are you" in text:
        return "I'm doing great! Thanks for asking. How about you?"

    elif re.search(r"sad|depressed|upset", text):
        return "I'm sorry you're feeling this way. Want to talk about it?"

    elif re.search(r"happy|excited", text):
        return "That's awesome! Great to hear 😊"

    # -----------------------------------------------
    # 6. Frequently Asked Things
    # -----------------------------------------------
    elif "your purpose" in text:
        return "My purpose is to assist and help users like you learn AI."

    elif "help" in text:
        return "Sure! I can tell time, date, solve math, chat with you, and answer basic questions."

    elif "joke" in text:
        return "Why don’t robots panic? 🤖 Because they have nerves of steel!"

    # -----------------------------------------------
    # 7. Goodbye
    # -----------------------------------------------
    elif re.search(r"bye|goodbye|exit|see you", text):
        return "Goodbye! Have a fantastic day! 👋"

    # -----------------------------------------------
    # 8. Default fallback response
    # -----------------------------------------------
    else:
        return (
            "I'm not sure I understand that yet 🤔\n"
            "But I can help with:\n"
            "• Telling time/date\n"
            "• Solving math\n"
            "• Small talk\n"
            "• Basic questions\n"
            "Try asking me something!"
        )


# ============================
# Main Chat Loop
# ============================

print("🤖 Chatbot Ready! Type 'exit' to stop.")

while True:
    user = input("You: ")
    
    if user.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break

    print("Chatbot:", respond(user))