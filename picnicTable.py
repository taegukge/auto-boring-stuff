def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-')) # center using -
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth)) # leftwidth using .
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 10, 6)
printPicnic(picnicItems, len(max(picnicItems.keys(), key=len)), len(str(max(picnicItems.values()))) + 1)
""" longest word in picnic item to decide left width;
    longest number (+1) to decide right width.
"""
