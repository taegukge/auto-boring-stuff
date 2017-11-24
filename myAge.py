### Age Test ###
print('How old are you?')
myAge = input()
if int(myAge) > 29:
    print("Hey, you're older than I am!")
elif int(myAge) == 29:
    print("Cousin, let's go bowling!")
elif int(myAge) < 29 and int(myAge) > 20:
    print("Whee, let's go grab a drink!")
elif int(myAge) < 21 and int(myAge) > 17:
    print("Taufiq is over there.")
elif int(myAge) < 18:
    print("Isn't it past your bedtime?")
else:
    print('Hey, put in a real age!')
