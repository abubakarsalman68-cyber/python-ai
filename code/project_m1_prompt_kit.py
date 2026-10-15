"""
AI Prompt Kit for a Local Business
"""

business_name = input("Enter your business name")
monthly_budget = int(input("Enter your monthly budgets:"))
City = input("Enter your city:")
main_customers = input("Enter your main customers:")
monthly_budget =int(input("Enter your monthly budget: "))

print()
print(f"Bussiness Name: {business_name}")
print(f"BussinessType: {business_name}")
print(f"City: {City}")
print(f"Main Customers: {main_customers}")
print(f"Monthly Budget: ${monthly_budget:}")



marketing = (
    f"Create a marketing strategy for {business_name}, a {business_name} located in {City}. "
    f"The main customers are {main_customers}. The monthly budget is ${monthly_budget:}."
)


customer_service =(
    f"Create a customer service strategy for {business_name}, a {Business_type} located in {City}. "
    f"The main customers are {main_customers}. The monthly budget is ${monthly_budget:}."
)


growth (
    f"Create a growth strategy for {business_name}, a {Business_type} located in {City}. "
    f"The main customers are {main_customers}. The monthly budget for growth is ${monthly_budget}"
)