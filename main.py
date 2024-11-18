import pandas as pd
from manage_inventory_funcs import add_to_inventory, delete_from_inventory, save_changes_to_excel_file, \
    create_data_frame

if __name__ == "__main__":

    file_path = "C:/Users/julia/Documents/dnd_programme/dnd_inventory.xlsx"
    excel_frame = pd.read_excel(file_path)
    print(excel_frame)
    inventory = dict(zip(excel_frame["Items"],excel_frame["Count"]))
    print(inventory)



    running = True
    while running:
        player_input = input("Welche Aktion willst du ausführen?: ").lower()

        if player_input ==  "help":
            print("""
                Du kannst folgende Commands ausführen:
                end - Programm beenden
                display - aktuelles Inventar ausgeben
                add - item zu Inventar hinzufügen
                remove - item aus Inventar entfernen
                change -  Schreibfehler korrigieren
                currency - Geldwerte verwalten
                  """)

        elif player_input == "end":
            running = False

        elif player_input == "display":
            print("\n", create_data_frame(inventory), "\n")

        elif player_input == "add":
            inventory = add_to_inventory(inventory)
            save_changes_to_excel_file(inventory, file_path)


        elif player_input == "remove":
            inventory = delete_from_inventory(inventory)
            save_changes_to_excel_file(inventory, file_path)

        else:
            print("Bitte gebe ein bekanntes Command ein. Diese kannst du mit help nachschlagen.")




    commands = ["add", "remove", "remove last", "currency", "display inventory","end", "help"]

    # mehr mit dataframe und pandas in testground ausprobieren