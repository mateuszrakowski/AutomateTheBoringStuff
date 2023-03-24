tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def tablePrint(table):
    colWidths = [0] * len(tableData)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])
        
    for x in range(len(table[0])):
        for y in range(len(table)):                
            print(table[y][x].rjust(colWidths[y]), end=" ")
        print("")


tablePrint(tableData)
