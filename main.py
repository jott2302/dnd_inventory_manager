import pandas as pd
from manage_inventory_funcs import save_changes_to_excel_file,create_data_frame, delete_whole_inventory, add_to_inventory, delete_from_inventory, correct_inventory_item

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
                clear - Inventar komplett, unwiederuflich, löschen
                  """)

        elif player_input == "end":
            running = False

        elif player_input == "display":
            print("\n", excel_frame, "\n")

        elif player_input == "add":
            excel_frame = add_to_inventory(excel_frame)
            save_changes_to_excel_file(excel_frame, file_path)

        elif player_input == "remove":
            excel_frame = delete_from_inventory(excel_frame)
            save_changes_to_excel_file(excel_frame, file_path)

        elif player_input == "clear":
            verification = input("Mit der Eingabe -verify- das gesamte Inventar löschen: ")
            if verification == "verify":
                excel_frame = delete_whole_inventory(excel_frame)
                save_changes_to_excel_file(excel_frame, file_path)
            else:
                print("Dein Inventar wurde nicht gelöscht.")

        elif player_input == "change":
            excel_frame = correct_inventory_item(excel_frame)
            save_changes_to_excel_file(excel_frame,file_path)


        else:
            print("Bitte gebe ein bekanntes Command ein. Diese kannst du mit help nachschlagen.")




    commands = ["add", "remove", "remove last", "currency", "display inventory","end", "help"]

    # mehr mit dataframe und pandas in testground ausprobieren