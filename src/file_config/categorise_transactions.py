import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    # # This is the default and can be omitted
    # api_key=os.environ.get("OPENAI_API_KEY"),
)

# Define the predefined categories
categories = ["Food & Drink", "Investment", "Recreation", "Utilities", "Groceries", "Travel", "Gifts"]

def categorize_transaction(transaction):
    # Call the ChatGPT API to generate category for the transaction
    prompt = f"Transaction: {transaction}\nCategories: {', '.join(categories)}\nCategory:"
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a financial transaction categoriser."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.6
    )
    category = response.choices[0].message.content
    if category in categories:
         return category
    else:
        return "Other"
