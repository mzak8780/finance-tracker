import pandas as pd
import matplotlib.pyplot as plt
import openai

FOOD_AND_DRINKS = ['eats','*eats', 'liquor', 'bar', 'sussex', 'pure gelato', 'chips', 'cafe', 'restaurant', 'mcdonalds', 'hotel', '*ubereats', 'foods', 'dan']
GROCERIES = ['wholefarms', 'coles', 'woolworths','iga']
RECREATION = ['sports', 'sport', 'ebay', 'basketball', 'syrenka', 'polart', 'football', '*gameday', 'jetts']
TRAVEL = ['palm', 'hotels', 'flights', 'retreat', 'hunterv']
INTERNAL = ['internal', 'round', 'maximiser']
UTILITIES = ['spotify','post', 'insuranceau', 'nsw', 'service', '*service', 'transportfornsw', 'bp','uber','7-eleven' , 'automotive', 'petrol', 'metro', 'petroleum', 'aami','nrma']
GIFTS = ['apple', '*rebeb', 'puma', 'nike', 'adidas', 'david', '*sunglasshut', 'iconic', 'politix', 'present', 'bag', 'ck', 'zara', 'rose', 'flowers', 'ikea', 'snooze', '*auto', 'rmwilliams_pos_au']
INVESTMENT = ['investment', 'anz']

class DataSchema:
    TYPE = "Type"
    DESCRIPTION = "Description"
    MONTH = "Month"
    YEAR = "Year"
    DEBIT = "Debit"
    CREDIT = "Credit"

def configureFile(path: str) -> pd.DataFrame:
    finances = pd.read_csv(path, na_values='n/a', parse_dates=['Date'], dayfirst=True)
    finances[DataSchema.DESCRIPTION] = finances[DataSchema.DESCRIPTION].astype(str).str.lower()

    finances[DataSchema.MONTH] = finances['Date'].dt.month.astype(str)
    finances[DataSchema.YEAR] = finances['Date'].dt.year.astype(str)
    finances[DataSchema.DEBIT] = finances[DataSchema.DEBIT].abs()
     
    # for index, row in finances.iterrows():
    #     description = list(finances.loc[index, DataSchema.DESCRIPTION].split(" "))

    #     if any(word in FOOD_AND_DRINKS for word in description[:25]):
    #         finances.loc[index, DataSchema.TYPE] = 'Food & Drinks'
    #     elif any(word in GROCERIES for word in description[:25]):
    #         finances.loc[index, DataSchema.TYPE] = 'Groceries'
    #     elif (any(word in RECREATION for word in description[:25])):
    #         finances.loc[index, DataSchema.TYPE] = 'Recreation'
    #     elif (any(word in TRAVEL for word in description[:45])):
    #         finances.loc[index, DataSchema.TYPE] = 'Travel'
    #     elif (any(word in UTILITIES for word in description[:25])):
    #         finances.loc[index, DataSchema.TYPE] = 'Utilities'
    #     elif (any(word in GIFTS for word in description[:25])):
    #         finances.loc[index, DataSchema.TYPE] = 'Personal Spending'
    #     elif (any(word in INVESTMENT for word in description[:35])):
    #         finances.loc[index, DataSchema.TYPE] = 'Investment'
    #     elif (any(word in INTERNAL for word in description[:25])):
    #         finances.loc[index, DataSchema.TYPE] = 'Internal'
    #         continue
    #     else: finances.loc[index, DataSchema.TYPE] = 'Other'

    return finances
