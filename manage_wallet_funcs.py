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
