
"""
Lesson 1.6: Prompt Cleaner

This program cleans a user's name and question,
estimates tokens, checks for Python-related text,
and builds a clean prompt for an AI tutor.
"""

# Ask for user details so the prompt can be personalised.
raw_name = input("Enter your name: ")
raw_question = input("Enter your question: ")

# Remove extra spaces and format the name for a clean greeting.
name = raw_name.strip().title()

# Clean the question so extra spaces and random capitals are reduced.
clean_question = raw_question.strip().capitalize()

# Replace an example bad word to demonstrate basic text cleaning.
clean_question = clean_question.replace("stupid", "***")

# Estimate tokens because long prompts may use more AI resources.
estimated_tokens = round(len(clean_question) / 4)

# Limit the question to 150 characters to keep the prompt short.
short_question = clean_question[:150]

# Check without case sensitivity so Python, PYTHON, and python all match.
mentions_python = "python" in clean_question.lower()

# Build a multi-line prompt with a greeting and clear instructions.
prompt = f"""You are a helpful Python tutor.
Greet the user by name: {name}.
Answer the user's question in simple language.
Keep your answer clear and easy to understand.
Question: {short_question}
"""

print("\n" + "=" * 40)
print("       PROMPT CLEANER RESULTS")
print("=" * 40)

print(f"User Name: {name}")
print(f"Cleaned Question: {clean_question}")
print(f"Characters: {len(clean_question)}")
print(f"Estimated Tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")

# Show a practice cost estimate using an example price per 1K tokens.
price_per_1k_tokens = 0.5
estimated_cost = estimated_tokens / 1000 * price_per_1k_tokens
print(f"Estimated Cost: {estimated_cost:.2f} PKR")

print("\n" + "=" * 40)
print("       FINAL AI PROMPT")
print("=" * 40)
print(prompt)
print("=" * 40)
