def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))
        

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):    # for number of items in addedItems
        inventory.setdefault(addedItems[i], 0)    # set amount to 0 unless already in inventory
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1    # add 1 to inventory for every addedItem
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(inv)
print(dragonLoot)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
