
"""
Lesson 1.5: AI Model Profile Card
"""

# Store model details using different data types
MODEL = "gemini-4-argon"
context_window = 1000000
price_per_1k_tokens = 0.5
runs_locally = False

# A low temperature helps keep answers focused
temperature = 0.2

# Display the model profile and data types
print("--- AI Model Profile Card ---")
print(f"Model: {MODEL} | Type: {type(MODEL)}")
print(f"Context Window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR | Type: {type(price_per_1k_tokens)}")
print(f"Runs Locally: {runs_locally} | Type: {type(runs_locally)}")

# Convert input to int so we can calculate the cost
tokens_used = int(input("\nHow many tokens does one chat use? "))

cost = tokens_used / 1000 * price_per_1k_tokens

print(f"Estimated cost per chat: {round(cost, 2)} PKR")

# Estimate monthly cost for 30 days
chats_per_day = int(input("How many chats per day? "))
monthly_cost = cost * chats_per_day * 30

print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")