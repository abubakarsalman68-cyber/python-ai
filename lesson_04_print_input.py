"""
Tool Name: AI Prompt Generator for Digital Agency Clients
Description: This script collects custom inputs from clients and dynamically 
generates tailored AI solution prompts for their business challenges.
"""

# Collect user details dynamically so the generated prompt is tailored to each client's unique context.
name = input("Enter your name: ")
business = input("Enter your business type: ")
problem = input("Enter one problem your business faces: ")

# Greet the user personally to create an engaging and interactive onboarding experience.
print(f"\nWelcome, {name}! Let's generate your custom AI prompt.")

# Separate raw inputs from the final output format to keep the prompt structure clean and reusable.
ai_prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print("\n--- Your Generated AI Prompt ---")
print(ai_prompt)