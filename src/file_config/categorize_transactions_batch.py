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
categories = ["Dining", "Investment", "Recreation", "Utilities", "Groceries", "Travel", "Gifts", "Clothing", "Health"]

# Estimate average token usage per transaction and max tokens
avg_tokens_per_transaction = 10  # Adjust based on actual average length of transactions
max_tokens = 4096

# Static parts of the prompt
system_message = "You are a financial transaction categoriser."
categories_list = f"Categories: {', '.join(categories)}"
prompt_structure = "Transactions:\n"
static_tokens = len(system_message.split()) + len(categories_list.split()) + len(prompt_structure.split()) + avg_tokens_per_transaction  # Approximate token count for static parts

# Calculate maximum number of transactions per batch
remaining_tokens = max_tokens - static_tokens
max_transactions_per_batch = remaining_tokens // avg_tokens_per_transaction

def categorize_transactions_batch(transactions):
    # Split transactions into batches
    batches = [transactions[i:i + max_transactions_per_batch] for i in range(0, len(transactions), max_transactions_per_batch)]

    categorized_results = []
    for batch in batches:
        prompt = f"{prompt_structure}"
        for transaction in batch:
            prompt += f"- {transaction}\n"
        prompt += f"{categories_list}\nCategorize each transaction with the most appropriate category strictly from the above list."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        batch_results = response.choices[0].message.content.splitlines()
        # Extract just the category from each response line
        for result in batch_results:
            if result.strip():
                print(result)
                # Assuming the format is "Transaction: Category"
                category = result.split(":")[-1].strip()
                if category not in categories:
                    category = "Other"
                categorized_results.append(category)
    return categorized_results
