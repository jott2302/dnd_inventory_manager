

def add_to_inventory(inventory):
    item = input("Welches Item willst du deinem Inventar hinzufügen?: ").lower()
    count = int(input(f"Anzahl der {item}: "))
    if item not in inventory:
        inventory.setdefault(item, count)
    else:
        new_count = inventory.get(item) + count
        inventory.update({item: new_count})




def delete_from_inventory(inventory):
    item = input("Welches Item soll aus dem Inventar genommen weden?: ").lower()
    count = int(input(f"Wie viele {item} sollen entfernt werden?: "))
    if count < inventory.get(item):
        new_count = inventory.get(item) - count
        inventory.update({item: new_count})
    else:
        inventory.pop(item)


backpack = {}
if __name__ == "__main__":
    add_to_inventory(backpack)
    print(backpack)
    delete_from_inventory(backpack)
    print(backpack)
    add_to_inventory(backpack)
    print(backpack)
    add_to_inventory(backpack)
    print(backpack)