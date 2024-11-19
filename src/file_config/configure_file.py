import pandas as pd
import matplotlib.pyplot as plt
from .categorize_transactions_batch import categorize_transactions_batch

class DataSchema:
    TYPE = "Type"
    DESCRIPTION = "Description"
    MONTH = "Month"
    YEAR = "Year"
    DEBIT = "Debit"
    CREDIT = "Credit"

def configureFile(path: str) -> pd.DataFrame:
    
    # Open file
    finances = pd.read_csv(path, na_values='n/a', parse_dates=['Date'], dayfirst=True)
    finances.dropna(subset=DataSchema.DEBIT, inplace=True)

     # Clean up data by shortening description 
    finances[DataSchema.DESCRIPTION] = finances[DataSchema.DESCRIPTION].astype(str).apply(lambda x: x[:30])

    # Remove internal transfers to other account
    finances = finances[finances[DataSchema.DESCRIPTION].str.contains("Internal|Everyday") == False]
    finances = finances.head(200) #Limit the amount of record calls to CHAT GPT

    # Assign Date values to Month and Year
    finances[DataSchema.MONTH] = finances['Date'].dt.month.astype(str)
    finances[DataSchema.YEAR] = finances['Date'].dt.year.astype(str)
    finances[DataSchema.DEBIT] = finances[DataSchema.DEBIT].abs()

    # Get unique descriptions that need to be categorized
    unique_transactions = finances[DataSchema.DESCRIPTION].unique()

    # Categorize transactions in bulk
    if unique_transactions.size > 0:
        categorized_results = categorize_transactions_batch(unique_transactions)

        # Map results back to transactions
        transaction_category_map = dict(zip(unique_transactions, categorized_results))

        # Assign categories to the DataFrame
        finances[DataSchema.TYPE] = finances[DataSchema.DESCRIPTION].apply(lambda x: transaction_category_map.get(x, "Other"))

    else:
        # If no transactions need categorization
        finances[DataSchema.TYPE] = "Other"

    finances.to_csv("data/testData_2.csv")

    return finances
