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


def correct_inventory_item(inventory):
    item_old = input("Welches Item soll korrigiert werden?: ")
    item_new = input("Wie heißt das neue Item?: ")
    inventory[item_new] = inventory.pop(item_old)

def save_changes_to_excel_file(df_excel, data_path):
    with pd.ExcelWriter(data_path, mode="a", if_sheet_exists="replace") as writer:
        df_excel.to_excel(writer, index=False, sheet_name="Inventory")


def create_data_frame(dict_inventory):
    return pd.DataFrame({"Items": dict_inventory.keys(), "Count": dict_inventory.values()})

def delete_whole_inventory(df_excel):
    empty_df = df_excel[0:0]
    return empty_df
