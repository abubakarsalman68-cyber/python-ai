

"""
Lesson 1.4: Build an AI prompt from user input.
"""

# Ask for details so the prompt matches the user's business
name = input("Enter your name: ")
business = input("Enter your business type: ")
problem = input("What problem does your business face? ")

# Use the answers to create a personalized AI prompt
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(f"\nWelcome, {name}!")
print("\n--- Your AI Prompt ---")
print(prompt)
