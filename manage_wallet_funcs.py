import pandas as pd

def manage_currencies(df):
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


def convert_between_currencies(from_currency, to_currency, amount):
    if amount < 0:
        print("Die Währung kann nicht negativ sein.")
        return False
    currency_ordered = ["CP", "SP", "GP", "PP"]
    if from_currency not in currency_ordered or to_currency not in currency_ordered:
        print("Die Währung muss CP, SP, GP oder PP sein.")
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
        print("Keine Konvertierung notwengig.")
        return False

def convert_to_excel_wallet(excel_frame, from_currency, to_currency, amount):
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
    print(f"{amount} {from_currency} wurden in {converted_amount} {to_currency} umgewandelt.")
    return excel_frame

