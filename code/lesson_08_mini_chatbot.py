

"""
Lesson 1.8: Mini Project - Business Helper Chatbot

This rule-based chatbot helps customers with business FAQs,
remembers their name, handles complaints, and tracks unanswered questions.
"""

BOT = "Sweet Crumbs Bot"

print(f"{BOT}: Welcome! I can help with prices, opening hours, location, and orders.")
print(f"{BOT}: Type 'bye' to end the chat.")

# Ask once so the bot remembers the customer's name during the conversation.
name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "Friend"

print(f"{BOT}: Nice to meet you, {name}!")

# Counters help the business understand customer questions and complaints.
count = 0
unanswered = 0
complaints = 0

while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thanks for visiting.")
        break

    elif message == "":
        print(f"{BOT}: Please type a question.")

    # Why: Complaints come first so unhappy customers get priority.
    elif "refund" in message or "complaint" in message or "late" in message:
        complaints += 1
        print(f"{BOT}: Sorry about that, {name}. A manager will help you.")

    # Bonus: Offer a human handover when requested.
    elif "human" in message or "agent" in message:
        print(f"{BOT}: Connecting you to a human...")
        break

    elif "hour" in message or "open" in message or "time" in message:
        print(f"{BOT}: We are open from 9 AM to 10 PM every day.")

    elif "price" in message or "cost" in message or "how much" in message:
        print(f"{BOT}: Cakes start at 1,500 PKR. Cupcakes are 250 PKR each.")

    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: We are on Main Boulevard, Lahore.")

    elif "order" in message or "delivery" in message:
        print(f"{BOT}: You can order through our business WhatsApp.")

    # Why: Exact greeting checks avoid matching 'hi' inside 'which'.
    elif message in ["hi", "hello"] or message.startswith("salam"):
        print(f"{BOT}: Hello, {name}! How can I help you?")

    else:
        unanswered += 1

        # Why: This prompt can be sent to an AI model in Module 2.
        prompt = (
            f"You are a friendly assistant for {BOT}. "
            f"Answer the customer's question in 2 short lines: {message}"
        )

        print(f"{BOT}: I don't know that answer yet.")
        print(f"AI prompt for Module 2: {prompt}")

print("=" * 40)
print("CHAT SUMMARY")
print(f"Total messages: {count}")
print(f"Unanswered questions: {unanswered}")
print(f"Complaints received: {complaints}")
print("=" * 40)
