
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





Assalam-o-Alaikum.

My project is called AI Prompt Kit for a Local Business.

The main problem is that many small business owners want to use AI, but they do not know what prompts to write.

My Python program asks five questions: business name, business type, city, main customers, and monthly budget.

After collecting these details, it generates three professional prompts.

The first prompt is for social media marketing. The second is for replying politely to unhappy customers. The third suggests three low-cost AI ideas for business growth.

I can copy these prompts into Ollama, ChatGPT, or Claude and test the results.

I will check whether the AI answers are useful and whether the AI invents prices, offers, or other facts.

In the future, I would like to improve this project by adding more prompt types and comparing different AI models.

This tool can help small business owners save time and use AI more effectively.

Thank you.