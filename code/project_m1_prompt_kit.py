
"""
AI Prompt Kit for local businesses.
This tool creates 3 useful AI prompts for small business owners.
"""

# Ask for business details so prompts can be personalised.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")

# Convert the monthly budget from text into an integer.
budget = int(input("Monthly budget (PKR): "))

# Display a clear heading so the user can identify their prompt kit.
print("\n" + "=" * 41)
print(f"   AI Prompt Kit for {business_name}")
print("=" * 41)

# Prompt 1: Include the audience and tone to make marketing content useful.
marketing_prompt = f"""
Act as a professional social media marketer.
Create one creative Instagram post idea for {business_name},
a {business_type} in {city}.
Target audience: {customers}.
Use a friendly tone and include one call to action.
"""

print("\n[1] Marketing")
print(marketing_prompt)

# Prompt 2: Give the AI a role and a clear customer-service task.
customer_service_prompt = f"""
Act as the customer service manager of {business_name}.
Write a polite reply to an unhappy customer whose order
arrived late. Apologise sincerely and offer a suitable solution.
Business type: {business_type}.
Use a friendly and professional tone.
Do not promise an unapproved discount.
"""

print("\n[2] Customer Service")
print(customer_service_prompt)

# Prompt 3: Mention the budget so growth ideas remain affordable.
growth_prompt = f"""
Act as a small-business AI consultant.
Suggest exactly 3 low-cost AI ideas for {business_name},
a {business_type} in {city}.
Target customers: {customers}.
Monthly budget: {budget} PKR.
Explain the benefit and estimated monthly cost of each idea.
Keep the total estimated cost within the budget.
Do not invent prices; clearly label estimates that need verification.
"""

print("\n[3] Growth")
print(growth_prompt)

print("\n" + "=" * 41)
print("Your 3 AI prompts are ready!")
print("=" * 41)





