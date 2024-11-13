import os
import pandas as pd


file_path = "C:/Users/julia/Documents/dnd_programme/dnd_inventory.xlsx"
file = "dnd_inventory.xlsx"

dataframe1 = pd.read_excel(file_path)

running = True
while running:
    player_input = input("Welche Aktion willst du ausführen?: ").lower()
    if player_input == "help":
        print("""
            Du kannst folgende Commands ausführen:
            end - Programm beenden
            display - aktuelles Inventar ausgeben
            add - item zu Inventar hinzufügen
            remove - item aus Inventar entfernen
            remove last - aktuellstes Item entfernen
            currency - Geldwerte verwalten
              """)
    elif player_input == "end":
        running = False
    elif player_input == "display":
        print("\n", dataframe1, "\n")

    else:
        print("Bitte gebe ein bekanntes Command ein. Diese kannst du mit help nachschlagen.")




commands = ["add", "remove", "remove last", "currency", "display inventory","end", "help"]