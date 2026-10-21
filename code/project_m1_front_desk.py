
"""Sweet Crumbs bakery front desk chatbot.
Answers FAQs, calculates order prices, and prepares AI prompts.
"""

BOT_NAME = "Sweet Crumbs Desk"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.10

print("=" * 50)
print(f"{BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

customer_name = input(
    f"{BOT_NAME}: What is your name? "
).strip().title()

if customer_name == "":
    customer_name = "Customer"

message_count = 0
rules_answered = 0
unanswered_count = 0
quote_count = 0
total_quoted_value = 0
total_ai_cost = 0.0
complaint_count = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()

    if message == "":
        print(f"{BOT_NAME}: Please type a message.")
        continue

    if message == "bye":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    message_count += 1

    # Complaints come first so unhappy customers get human support.
    if (
        "refund" in message
        or "complaint" in message
        or "late" in message
    ):
        print(
            f"{BOT_NAME}: Sorry about that. "
            "A manager will call you within 1 hour."
        )
        rules_answered += 1
        complaint_count += 1

    elif (
        message == "hi"
        or message.startswith("hi ")
        or message == "hello"
        or message.startswith("hello ")
        or message == "salam"
    ):
        print(
            f"{BOT_NAME}: Hello, {customer_name}! "
            "Welcome to Sweet Crumbs bakery."
        )
        rules_answered += 1

    elif (
        "hours" in message
        or "timing" in message
        or "open" in message
    ):
        print(
            f"{BOT_NAME}: We are open 9 am to 10 pm, every day."
        )
        rules_answered += 1

    elif (
        "location" in message
        or "address" in message
        or "where" in message
    ):
        print(
            f"{BOT_NAME}: We are on Main Market Road. "
            "Please confirm the exact address with our staff."
        )
        rules_answered += 1

    elif "delivery" in message or "deliver" in message:
        print(
            f"{BOT_NAME}: Delivery costs {DELIVERY_FEE:,} PKR. "
            f"Orders of {FREE_DELIVERY_LIMIT:,} PKR or more "
            "after discount get free delivery."
        )
        rules_answered += 1

    elif (
        "fee" in message
        or "charges" in message
        or "price" in message
    ):
        print(
            f"{BOT_NAME}: Type /quote to calculate your order price."
        )
        rules_answered += 1

    elif message == "/quote":
        item = input(
            f"{BOT_NAME}: Which item? "
        ).strip().lower()

        quantity_text = input(
            f"{BOT_NAME}: How many? "
        ).strip()

        # Validate quantity so letters do not crash the program.
        if not quantity_text.isdigit():
            print(
                f"{BOT_NAME}: Please enter a valid whole number."
            )

        elif int(quantity_text) <= 0:
            print(
                f"{BOT_NAME}: Quantity must be greater than zero."
            )

        else:
            quantity = int(quantity_text)

            if item == "cupcake":
                unit_price = 250
            elif item == "brownie":
                unit_price = 300
            elif item == "chocolate cake":
                unit_price = 1500
            else:
                unit_price = 0

            if unit_price == 0:
                print(
                    f"{BOT_NAME}: Sorry, {item} "
                    "is not on our menu."
                )

            else:
                subtotal = unit_price * quantity
                discount = 0

                if quantity >= 10:
                    discount = round(subtotal * 0.10)

                discounted_subtotal = subtotal - discount

                # Delivery is checked after discount as the brief requires.
                if discounted_subtotal >= FREE_DELIVERY_LIMIT:
                    delivery = 0
                else:
                    delivery = DELIVERY_FEE

                total = discounted_subtotal + delivery

                print(
                    f"{BOT_NAME}: {quantity:,} x {item} "
                    f"= {subtotal:,} PKR"
                )
                print(
                    f"     Discount: -{discount:,} PKR "
                    f"| Delivery: {delivery:,} PKR"
                )
                print(f"     Total: {total:,} PKR")

                quote_count += 1
                total_quoted_value += total

    else:
        unanswered_count += 1

        question = message.capitalize()[:150]
        estimated_tokens = round(len(question) / 4)

        # Private questions stay local to protect customer information.
        is_private = (
            "phone" in question.lower()
            or "cnic" in question.lower()
            or "my address" in question.lower()
            or "home address" in question.lower()
        )

        if is_private:
            chosen_model = "llama3.2 (local, private)"
            estimated_cost = 0.0
        else:
            chosen_model = "small cloud model (cheap)"
            estimated_cost = (
                estimated_tokens / 1000
                * CLOUD_PRICE_PER_1K_TOKENS
            )
            total_ai_cost += estimated_cost

        print(
            f"{BOT_NAME}: Good question! Routed to: "
            f"{chosen_model} (~{estimated_tokens} tokens)"
        )

        prompt = f"""You are the assistant of Sweet Crumbs bakery.
Answer {customer_name} in 2 short lines.
Do not invent prices, opening hours, or promises.
If you do not know a business fact, ask staff to confirm it.
Question: {question}"""

        print("     Prompt:")
        print(prompt)

print("=" * 50)
print("Session report")
print(
    f"Messages: {message_count} | "
    f"Answered by rules: {rules_answered} | "
    f"Unanswered: {unanswered_count}"
)
print(
    f"Quotes: {quote_count} | "
    f"Quoted value: {total_quoted_value:,} PKR"
)
print(f"Total estimated AI cost: {total_ai_cost:.4f} PKR")
print(f"Complaints received: {complaint_count}")
print("=" * 50)
