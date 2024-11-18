import pandas as pd

def add_to_inventory(inventory):
    item = input("Welches Item willst du deinem Inventar hinzufügen?: ").lower()
    count = int(input(f"Anzahl an {item}: "))
    if item not in inventory:
        inventory.setdefault(item, count)
    else:
        new_count = inventory.get(item) + count
        inventory.update({item: new_count})
    return inventory

def delete_from_inventory(inventory):
    item = input("Welches Item soll aus dem Inventar genommen weden?: ").lower()
    count = int(input(f"Wie viele {item} sollen entfernt werden?: "))
    if count < inventory.get(item):
        new_count = inventory.get(item) - count
        inventory.update({item: new_count})
    else:
        inventory.pop(item)
    return inventory

def correct_inventory_item(inventory):
    item_old = input("Welches Item soll korrigiert werden?: ")
    item_new = input("Wie heißt das neue Item?: ")
    inventory[item_new] = inventory.pop(item_old)

def save_changes_to_excel_file(dict_inventory:dict , data_path):
    df_inventory = create_data_frame(dict_inventory)
    with pd.ExcelWriter(data_path, mode="a", if_sheet_exists="replace") as writer:
        df_inventory.to_excel(writer, index=False, sheet_name="Inventory")

def create_data_frame(dict_inventory):
    return pd.DataFrame({"Items": dict_inventory.keys(), "Count": dict_inventory.values()})
