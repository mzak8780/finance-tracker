import pandas as pd
import matplotlib.pyplot as plt
from .categorise_transactions import categorize_transaction

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

    # Remove internal transfers to other accoun
    finances = finances[finances[DataSchema.DESCRIPTION].str.contains("Internal|Everyday") == False]
    # finances = finances.head(1000)

    # Assign Date values to Month and Year
    finances[DataSchema.MONTH] = finances['Date'].dt.month.astype(str)
    finances[DataSchema.YEAR] = finances['Date'].dt.year.astype(str)
    finances[DataSchema.DEBIT] = finances[DataSchema.DEBIT].abs()

    for index, row in finances.iterrows():
        finances.loc[index, DataSchema.TYPE] = categorize_transaction(finances.loc[index, DataSchema.DESCRIPTION])

    finances.to_csv("data/testData.csv")

    return finances
