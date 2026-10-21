
# Project M1 Part 2 — Front Desk Chatbot Design

## 1. Business Introduction

**Business Name:** Sweet Crumbs Bakery

**Project Purpose:** This chatbot helps customers get bakery information, calculate order prices, and prepare AI prompts for questions that need additional help.

## 2. Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | Sorry about that. A manager will call you within 1 hour. |
| Greeting | hi, hello, salam | Welcome to Sweet Crumbs bakery. |
| Opening Hours | hours, timing, open | We are open 9 am to 10 pm every day. |
| Location | location, address, where | We are on Main Market Road. Confirm the exact address with staff. |
| Delivery | delivery, deliver | Delivery costs 200 PKR. Orders of 3,000 PKR or more after discount get free delivery. |
| Price Help | fee, charges, price | Type /quote to calculate your order price. |

### Rule Order

The complaint rule comes first so unhappy customers can receive human support quickly. Greeting rules use exact matching or `startswith()` to avoid false matches inside words such as `which`.

## 3. Business Rules

| Rule | Value |
|---|---|
| Cupcake Price | 250 PKR each |
| Brownie Price | 300 PKR each |
| Chocolate Cake Price | 1,500 PKR each |
| Bulk Discount | 10% off for 10 or more items |
| Delivery Fee | 200 PKR |
| Free Delivery | Discounted subtotal of 3,000 PKR or more |
| Private Keywords | phone, cnic, my address, home address |
| Local Model | llama3.2 |
| Estimated Cloud Price | 0.10 PKR per 1,000 tokens |
| Token Estimation | Approximately one token per four characters |

## 4. Price Calculation Logic

The chatbot calculates the subtotal first, applies the bulk discount, checks the discounted subtotal for free delivery, and then calculates the final total.

**Example: 12 Cupcakes**

- Subtotal: 12 × 250 = 3,000 PKR
- Discount: 10% = 300 PKR
- Discounted subtotal: 2,700 PKR
- Delivery fee: 200 PKR
- Final total: 2,900 PKR

Delivery is charged because the discounted subtotal is below 3,000 PKR.

## 5. Rule Test Results

Run each test and update the Pass? column according to the actual result.

| You Type | Expected Result | Pass? |
|---|---|---|
| `  WHAT are your hours  ` | Opening hours reply | Not tested |
| `which cake is best?` | AI fallback, not greeting | Not tested |
| `my order is late` | Manager complaint reply | Not tested |
| `/quote`, cupcake, quantity 1 | 200 PKR delivery fee | Not tested |
| `/quote`, chocolate cake, quantity 3 | 4,500 PKR subtotal, 0 discount, 0 delivery | Not tested |
| `/quote`, cupcake, quantity 10 | 10% discount applied | Not tested |
| `/quote`, pizza, quantity 1 | Not on our menu | Not tested |
| Question containing `phone` or `cnic` | Local model selected, zero estimated cost | Not tested |
| Press Enter without text | Asks the customer to type a message | Not tested |
| `BYE` | Goodbye message and session report | Not tested |

## 6. Design Notes

- Constants use uppercase names for easy identification.
- Customer input is cleaned using `strip()` and `lower()`.
- The customer name is requested once before the main loop.
- Private questions are routed to a local model to help protect personal information.
- Unknown questions produce a prompt that can be copied into an AI model.
- The session report summarizes messages, answers, quotes, quoted value, estimated AI cost, and complaints.

**Note:** The chatbot prints AI prompts but does not automatically send them to Ollama. The cloud price is an example estimate.
