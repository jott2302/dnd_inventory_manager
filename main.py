import pandas as pd
import os.path
from manage_inventory_funcs import save_changes_to_excel_file,create_data_frame, delete_whole_inventory, add_to_inventory, delete_from_inventory, correct_inventory_item
from manage_wallet_funcs import manage_currencies, convert_to_excel_wallet
from excel_file_setup import check_file_path
if __name__ == "__main__":

    file_path = fr"{os.getcwdb().decode()}/excel_table/dnd_inventory.xlsx".replace(r"\\", "/")
    check_file_path(file_path)
    excel_inventory = pd.read_excel(file_path, sheet_name="Inventory")
    excel_wallet = pd.read_excel(file_path, sheet_name="Wallet")


    running = True
    while running:
        player_input = input("Welche Aktion willst du ausführen?: ").lower()

        if player_input ==  "help":
            print("""
                Du kannst folgende Commands ausführen:
                end - Programm beenden
                inv - aktuelles Inventar ausgeben
                add - item zu Inventar hinzufügen
                remove - item aus Inventar entfernen
                change -  Schreibfehler korrigieren
                wallet - Geldwerte verwalten
                convert - Geldwerte umtauschen
                clear - Inventar komplett, unwiederuflich, löschen
                  """)

        elif player_input == "end":
            running = False

        elif player_input == "inv":
            print("\n", excel_inventory, "\n")

        elif player_input == "add":
            excel_inventory = add_to_inventory(excel_inventory)
            save_changes_to_excel_file(excel_inventory, file_path, "Inventory")

        elif player_input == "remove":
            excel_inventory = delete_from_inventory(excel_inventory)
            save_changes_to_excel_file(excel_inventory, file_path, "Inventory")

        elif player_input == "clear":
            verification = input("Mit der Eingabe -verify- das gesamte Inventar löschen: ")
            if verification == "verify":
                excel_inventory = delete_whole_inventory(excel_inventory)
                save_changes_to_excel_file(excel_inventory, file_path, "Inventory")
            else:
                print("Dein Inventar wurde nicht gelöscht.")

        elif player_input == "change":
            excel_inventory = correct_inventory_item(excel_inventory)
            save_changes_to_excel_file(excel_inventory,file_path, "Inventory")

        elif player_input == "wallet":
            print("\n", excel_wallet, "\n")
            manage_currencies(excel_wallet)
            save_changes_to_excel_file(excel_wallet, file_path, "Wallet")
            print("\n", excel_wallet, "\n")

        elif player_input == "convert":
            print("\n", excel_wallet, "\n")
            have_currency = input("Welche Währung willst du umtauschen CP, SP, GP oder PP?: ").upper()
            print()
            want_currency = input(f"In welche Währung soll dein {have_currency} umgetauscht werden?: ").upper()
            print()
            currency_amount = int(input(f"Wie viel {have_currency} soll in {want_currency} umgetauscht werden?: "))
            convert_to_excel_wallet(excel_wallet, have_currency, want_currency, currency_amount)
            save_changes_to_excel_file(excel_wallet, file_path, "Wallet")
            print("\n", excel_wallet, "\n")


        else:
            print("Bitte gebe ein bekanntes Command ein. Diese kannst du mit help nachschlagen.")

