def addToInventory(inventory, addedItems):
    # your code goes here
    new={}
    for i in dragonLoot:
        
        inventory.setdefault(i,0)
        inventory[i]=inventory[i]+1

    new=inventory
    return new
    
def displayInventory(count):
    total =0
    print('Inventory:')
    for k,v in count.items():
            print(str(v)+' '+k)
            total=total+v
    print()
    print('Total number of itmes: '+str(total))
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
