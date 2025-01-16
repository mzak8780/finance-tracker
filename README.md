# Finance Tracker

## Description
The **Finance Tracker** is a tool designed to automatically categorize your transactions and provide visual insights into your spending habits. By utilizing **ChatGPT** for categorization and **Python** alongside **pandas**, this tool generates an informative graph based on the categorized data, allowing users to better understand their financial patterns.

## Key Features
- **Transaction Categorization**: Automatically categorizes transactions into predefined categories using **ChatGPT**'s natural language processing capabilities. This helps streamline the tracking process, ensuring accuracy and ease of use.
- **Data Processing**: Utilizes **Python** and the **pandas** library to efficiently process and analyze transaction data, offering robust handling of various datasets.
- **Spending Analysis**: Generates visually appealing graphs using **Matplotlib**, allowing users to visualize their spending patterns over time and make informed financial decisions.

## Technologies Used
- **ChatGPT**: Employed for transaction categorization based on descriptions.
- **Python**: The primary scripting language for data processing and automation.
- **pandas**: A Python library for efficient data manipulation and analysis.
- **Matplotlib**: A plotting library for visualizing spending trends and data insights.

## Process Flow
- Transactions are downloaded from personal online banking website
- Path to transactions is added to main.py
- Run the program 'python3 main.py'
- ChatGPT will process each transaction based on the description and assign it to one of several categories
- Graph will be generated, providing visual for spending by category and time 
