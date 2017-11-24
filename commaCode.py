### Comma code ###
# Separates list into sentence

def comma(lis):
    spam = "'" + lis[0] + ", "
    for i in lis[1:int(len(lis) - 1)]:
        spam = spam + i + ", "
    spam = spam + "and " + lis[len(lis) - 1] + "'."
    print(spam)

ham = ['apples', 'bananas', 'tofu', 'cats', 'belts', 'cords', 'shoes', 'pants']
comma(ham)
