import pandas as pd

def manage_currencies(df: pd.DataFrame):
    """
    Adjusts the amount of a specified currency in the dataframe.

    Parameters:
        df (pandas.DataFrame): A dataframe with "Currency" and "Amount" columns.

    Returns:
        pandas.DataFrame: The updated dataframe.

    Description:
        Allows the user to select a currency (CP, SP, GP, PP) and modify its amount
        by entering a positive or negative value. Prevents amounts from dropping below zero.
        Enter "0" to exit the process.
    """
    while True:
        currency = input("Welche Währung soll angeglichen werden?(0 - cancel): ").upper()
        if currency in ["CP","SP","GP","PP"]:
            try:
                amount = int(input("Bitte bestimme mit +/- und dem Betrag die Änderung: "))
                current_amount = df.loc[df["Currency"] == currency, "Amount"].iloc[0]
                new_amount = current_amount + amount
                if new_amount < 0:
                    print(f"Die Menge an {currency} kann nicht unter 0 fallen. Aktuell hast du {current_amount} {currency}")
                else:
                    df.loc[df["Currency"] == currency, "Amount"] = new_amount
                    print("\n", df, "\n")
            except ValueError:
                print("Bitte gib einen gültigen Betrag ein (Bsp. +10 oder -5).")
        elif currency == "0":
            print("Keine weiteren Änderungen.")
            return df
        else:
            print("Ungültige Eingabe. Bitte wähle CP, SP, GP, PP oder 0.")


def convert_between_currencies(from_currency: str, to_currency: str, amount: int):
    """
      Converts an amount between two specified currencies.

      Parameters:
          from_currency (str): The currency to convert from ("CP", "SP", "GP", "PP").
          to_currency (str): The currency to convert to ("CP", "SP", "GP", "PP").
          amount (int): The amount to be converted. Must be a non-negative integer.

      Returns:
          float or bool: The converted amount as a float, or False if the input is invalid
                         or no conversion is necessary.

      Description:
          The function calculates conversions based on a 1:10 ratio between adjacent currencies.
          It validates the input and ensures both currencies are valid and that the amount
          is non-negative.
      """
    currency_ordered = ["CP", "SP", "GP", "PP"]
    if not check_for_valid_currency_and_integer_amount(from_currency, to_currency, amount):
        return False
    if amount < 0:
        print("Die Währung kann nicht negativ sein.")
        return False
    conversion_rate = 10
    from_index = currency_ordered.index(from_currency)
    to_index = currency_ordered.index(to_currency)
    currency_difference = to_index - from_index

    if currency_difference > 0:
        return amount / (conversion_rate ** currency_difference)
    elif currency_difference < 0:
        return amount * (conversion_rate **abs(currency_difference))
    else:
        print("Keine Konvertierung notwendig.")
        return False

def convert_to_excel_wallet(excel_frame: pd.DataFrame, from_currency: str, to_currency: str, amount: int):
    """
    Converts a specified amount from one currency to another in an Excel-like dataframe.

    Parameters:
        excel_frame (pd.DataFrame): A DataFrame as an Excel-File to open and change.
        from_currency (str): The currency to convert from ("CP", "SP", "GP", "PP").
        to_currency (str): The currency to convert to ("CP", "SP", "GP", "PP").
        amount (int): The amount to be converted. Must be a non-negative integer.

    Returns:
        The manipulated or unchanged excel_frame depending on the validity of the amount.

    Description:
        This function checks if there is a sufficient balance in `from_currency` to perform
        the conversion. If successful, it deducts the amount from `from_currency`, adds the
        equivalent amount to `to_currency`, and ensures conversions yield whole numbers.
        If any condition is not met, the dataframe remains unchanged, and an appropriate
        message is printed.
    """

    if not check_for_valid_currency_and_integer_amount(from_currency, to_currency, amount):
        return False
    current_balance = excel_frame.loc[excel_frame["Currency"] == from_currency, "Amount"].iloc[0]
    if current_balance < amount:
        print(f"Nicht genügend {from_currency} um in {to_currency} umzuwandeln.")
        return excel_frame
    converted_amount = convert_between_currencies(from_currency, to_currency, amount)
    if not converted_amount:
        return excel_frame
    if not converted_amount.is_integer():
        print("Die Umrechnung ist nicht möglich, da sie keine ganze Zahl ergibt.")
        return excel_frame
    excel_frame.loc[excel_frame["Currency"] == from_currency, "Amount"] -= amount
    excel_frame.loc[excel_frame["Currency"] == to_currency, "Amount"] += converted_amount
    print(f"{amount} {from_currency} wurden in {int(converted_amount)} {to_currency} umgewandelt.")
    return excel_frame


def check_for_valid_currency_and_integer_amount(from_currency, to_currency, amount):
    currencies = ["CP", "SP", "GP", "PP"]
    if from_currency not in currencies or to_currency not in currencies:
        print("Die Währung muss CP, SP, GP oder PP sein.")
        return False
    if not isinstance(amount, int):
        print("Die Währung muss als integer Typ angegeben werden.")
        return False
    else:
        return True