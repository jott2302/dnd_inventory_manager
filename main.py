import os
from operator import index

import pandas as pd
from manage_inventory_funcs import add_to_inventory, delete_from_inventory


file_path = "C:/Users/julia/Documents/dnd_programme/dnd_inventory.xlsx"
excel_frame = pd.read_excel(file_path)
print(excel_frame)
inventory = dict(zip(excel_frame["Items"],excel_frame["Count"]))
excel_frame.to_excel(file_path, index=False, sheet_name="Inventory")
print(inventory)



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
            change -  Schreibfehler korrigieren
            currency - Geldwerte verwalten
              """)

    elif player_input == "end":
        running = False

    elif player_input == "display":
        print("\n", excel_frame, "\n")

    elif player_input == "add":
        add_to_inventory(inventory)
        excel_frame = pd.DataFrame(list(inventory.items()), columns=["Items", "Count"])
        with pd.ExcelWriter(file_path, mode="a", if_sheet_exists="replace") as writer:
            excel_frame.to_excel(writer, index=False, sheet_name="Inventory")
        #als funktion zusammenfassen!!



    else:
        print("Bitte gebe ein bekanntes Command ein. Diese kannst du mit help nachschlagen.")




commands = ["add", "remove", "remove last", "currency", "display inventory","end", "help"]