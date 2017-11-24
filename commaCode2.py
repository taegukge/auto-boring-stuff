### Comma code ###
# Separates list into sentence

def comma(lis):
    return (' and '.join(lis) if len(lis) <= 2    # .join joins elements in list
        else '{}, and {}'.format(', '.join(lis[:-1]), lis[-1]))    # .format places elements into {} (1st is all elements in list except last in ', ' and 2nd is last element

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(1 + len(spam)):
    lis = spam[:i]
    s = comma(lis)
    print(i, lis, repr(s))
