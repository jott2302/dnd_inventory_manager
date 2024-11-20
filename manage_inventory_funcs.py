import pandas as pd

def add_to_inventory(df):
    item = input("Welches Item willst du deinem Inventar hinzufügen?: ").lower()
    count = int(input(f"Anzahl an {item}: "))
    if item in df["Items"].values:
        df.loc[df["Items"] == item, "Count"] += count
    else:
        df.loc[len(df)] = [item, count]
    return df


def delete_from_inventory(df):
    item = input("Welches Item soll aus dem Inventar genommen weden?: ").lower()
    count = int(input(f"Wie viele {item} sollen entfernt werden?: "))
    if item in df["Items"].values:
        current_item_count = df.loc[df["Items"] == item, "Count"].iloc[0]
        if count < current_item_count:
            df.loc[df["Items"] == item, "Count"] -= count
        else:
            df = df[df["Items"] != item].reset_index(drop=True)
    else:
        print(f"Item {item} wurde nicht in dem Inventar gefunden!")
    return df


def correct_inventory_item(df):
    item_old = input("Welches Item soll korrigiert werden?: ").lower()
    item_new = input("Wie heißt das neue Item?: ").lower()
    if item_old in df["Items"].values:
        df.loc[df["Items"] == item_old, "Items"] = item_new
        print(f"{item_old} wurde erfolgreich in {item_new} umgeändert.")
    else:
        print(f"{item_old} konnte nicht im Inventar gefunden werden.")
    return df


def save_changes_to_excel_file(df_excel, data_path, sheet):
    with pd.ExcelWriter(data_path, mode="a", if_sheet_exists="replace") as writer:
        df_excel.to_excel(writer, index=False, sheet_name=sheet)


def create_data_frame(dict_inventory):
    return pd.DataFrame({"Items": dict_inventory.keys(), "Count": dict_inventory.values()})

def delete_whole_inventory(df_excel):
    empty_df = df_excel[0:0]
    return empty_df


#def set_up_inventory_and_wallet():
#    wallet_daten = {"Currency": ["PP", "GP", "SP", "CP"],
#                          "Amount": [0,0,0,0]}
#    excel_wallet = pd.DataFrame(wallet_daten)