### totalBrought ###
# Count number of each item brought

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0    # will be outputed number of items
    for k, v in guests.items():    # k = guest, v = item
        numBrought = numBrought + v.get(item, 0)    # each item will be added; .get if no item exists
    return numBrought

print('Number of things being brought:')
print(' - Apples    ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups    ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes    ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches    ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies    ' + str(totalBrought(allGuests, 'apple pies')))
