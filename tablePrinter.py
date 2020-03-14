def long(x):
    longest = len(tableData[x][0])
    j =0
    while True:
        if j == 4:
            break
        else:
            if longest < len(tableData[x][j]):
                longest = len(tableData[x][j])
        j=j+1
    return longest

def printTable():
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j == 0:
                print(tableData[j][i].rjust(first), end=' ')
            elif j == 1:
                print(tableData[j][i].rjust(second), end=' ')
            else:
                print(tableData[j][i].rjust(third), end=' ')
        print()
            
                
                   
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
                
                   
first = long(0)
second = long(1)
third = long(2)

printTable()

