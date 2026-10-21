
# Lesson 1.8: Business Helper Bot

**Course:** Python for AI  
**Module:** 1 — Python Basics for GenAI and Agentic AI

## 1. Project Overview

The Business Helper Bot is a rule-based chatbot built using Python. It helps customers get basic information about a local business by answering common questions.

This project demonstrates how a chatbot uses conditions, loops, variables, and user input to provide automatic replies.

## 2. Project Objectives

- Build a working rule-based chatbot.
- Understand how `while True` and `break` work.
- Use `if`, `elif`, and `else` to handle different questions.
- Store the customer's name and count messages.
- Handle complaints before other requests.
- Show a fallback response when a question is not recognized.

## 3. Features

- Greets customers.
- Answers business-related questions.
- Handles complaints.
- Provides opening hours, prices, location, and ordering information.
- Remembers the customer's name during the conversation.
- Counts total messages and unanswered questions.
- Displays a summary when the customer exits.

## 4. Technologies Used

- Python 3
- VS Code
- Git and GitHub

## 5. Project Structure

```text
project-folder/
├── README.md
└── code/
    └── lesson_08_mini_chatbot.py
```

## 6. How to Run the Project

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python code/lesson_08_mini_chatbot.py
```

4. Enter your name when prompted.
5. Ask questions about the business.
6. Type `bye` or `exit` to end the conversation.

## 7. Example Questions

- Hi
- What are your opening hours?
- How much is a cake?
- Where is your shop?
- I want to place an order.
- My order is late.
- Bye

## 8. Concepts Learned

- `input()` and `print()`
- Variables and data types
- String methods such as `.strip()` and `.lower()`
- Conditional statements
- `while True` loops
- The `break` statement
- Counters and f-strings
- Basic chatbot logic

## 9. Future Improvements

In Module 2, a Large Language Model (LLM) can be integrated to answer questions that the existing rules cannot recognize.

## 10. Conclusion

This project helped me understand how to build a simple chatbot using Python. It also demonstrated the importance of loops, conditional statements, rule ordering, and fallback responses in chatbot development.
