
"""
Lesson 1.7: Smart Model Router

This program chooses an AI model based on the task type,
estimates the cost, and warns about long requests.
"""

# Clean the task name so CODE, Code, and code work the same way.
task = input("Task (code / private / chat): ").strip().lower()

# Convert the token input to an integer for calculations.
tokens = int(input("Estimated tokens: "))

# Local models help keep private data on the user's own computer.
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k_tokens = 0.0
elif task == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k_tokens = 2.0
elif task == "chat":
    model = "small cloud model (cheap for chat)"
    price_per_1k_tokens = 0.5
else:
    model = "small cloud model (default)"
    price_per_1k_tokens = 0.5

# Calculate cost using an example price per 1,000 tokens.
# Example prices are for practice, not verified real API prices.
cost = tokens / 1000 * price_per_1k_tokens

# Long requests may use more tokens and cost more money.
if tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

# Check paid status and token length together using 'and'.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

if paid_user == "no" and tokens > 2000:
    print("Upgrade to send long requests.")

print("\n" + "=" * 45)
print("          SMART MODEL ROUTER")
print("=" * 45)

print(f"Task: {task}")
print(f"Chosen model: {model}")
print(f"Estimated tokens: {tokens}")
print(f"Estimated cost: {cost:.2f} PKR")
print(warning)

print("=" * 45)
