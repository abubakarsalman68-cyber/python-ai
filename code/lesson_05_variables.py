

"""
Lesson 1.5: AI Model Profile Card

This program stores AI model details, displays their data types,
and calculates the estimated cost of tokens used in a chat.
"""

# Store the AI model profile using four core data types.
model_name: str = "ollama3.2"
context_window: int = 8192
price_per_1k_tokens: float = 0.5
runs_locally: bool = True

# Display each value and its type to understand Python data types.
print("===== AI Model Profile Card =====")
print(f"Model Name: {model_name} | Type: {type(model_name)}")
print(f"Context Window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K Tokens: {price_per_1k_tokens} PKR | Type: {type(price_per_1k_tokens)}")
print(f"Runs Locally: {runs_locally} | Type: {type(runs_locally)}")

# Convert input text to an integer before doing calculations.
tokens_used = int(input("\nHow many tokens does one chat use? "))

# Divide by 1000 because the example price is for 1,000 tokens.
cost = tokens_used / 1000 * price_per_1k_tokens

print("\n===== Cost Estimate =====")
print(f"Tokens Used: {tokens_used}")
print(f"Estimated Cost: {round(cost, 2)} PKR")

# Ask for daily chats to estimate a 30-day budget.
chats_per_day = int(input("\nHow many chats per day? "))
monthly_cost = cost * chats_per_day * 30

print(f"Estimated Monthly Cost: {round(monthly_cost, 2)} PKR")
