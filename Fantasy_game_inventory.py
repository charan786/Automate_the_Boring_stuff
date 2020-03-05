stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def total(list):
    totalnum =0
    print('Inventory:')

    for k,v in list.items():
        print(str(v)+' '+k)
        totalnum = totalnum+v
    print('Total number of items: '+str(totalnum))

total(stuff)
