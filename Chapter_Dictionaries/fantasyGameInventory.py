stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    

def main():
    inv = addToInventory(stuff, dragonLoot)
    displayInventory(inv)

    
def displayInventory(inventory):
    total = 0    
    print("Inventory:")

    for k, v in inventory.items():
        print(f"{v} {k}")
        total += v
    
    print(f"Total number of items: {total}")


def addToInventory(inventory, addedItems):
    loot = {}

    # Count total items in addedItems
    for item in addedItems:
        loot.setdefault(item, 0)
        loot[item] += 1

    # Add items to inventory
    for k in loot:
        if k in inventory:
            inventory[k] += loot[k]
        else:
            inventory.setdefault(k, loot[k])

    # Return modified inventory
    return inventory


if __name__ == "__main__":
    main()
