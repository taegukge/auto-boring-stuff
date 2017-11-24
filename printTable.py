# printTable.py
# printTable - Prints list of strings as table with
# right-justified columns.

def printTable(tableData):
    colWidth = [0] * len(tableData) # column width list
    for i in range(len(tableData)): # find longest word in each column
        colWidth[i] = len(max(tableData[i], key=len))
    print(colWidth)
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidth[i] + 1, ' '), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
