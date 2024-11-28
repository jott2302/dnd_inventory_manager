import pandas as pd
import os.path


def create_excel_file(df_excel, data_path, mode, sheet):
    with pd.ExcelWriter(data_path, mode=mode) as writer:
        df_excel.to_excel(writer, index=False, sheet_name=sheet)

def check_file_path(excel_path):
    if not os.path.isdir("excel_table"):
        os.mkdir("excel_table")
        if not os.path.isfile("dnd_inventory.xlsx"):
            set_up_inventory_and_wallet(excel_path)
    else:
        print(f"Program läuft. Dein Inventar findest du unter {excel_path}")



def set_up_inventory_and_wallet(excel_path):
    wallet_daten = {"Currency": ["PP", "GP", "SP", "CP"],
                          "Amount": [0,0,0,0]}
    inv_daten = {"Items": [],
                 "Count": []}
    excel_wallet = pd.DataFrame(wallet_daten)
    excel_inventory = pd.DataFrame(inv_daten)
    create_excel_file(excel_inventory, excel_path, "w" ,"Inventory")
    create_excel_file(excel_wallet, excel_path , "a", "Wallet")
    print(f"Excel Datei wurde unter: {excel_path} erstellt.")
    return True