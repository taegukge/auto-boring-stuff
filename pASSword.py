print('Please state your name.')
name = input()
nm = ['Irene', 'irene']
if name in nm:
    print("Hi there, Irene! What's the secret password? Hint: Big Sean and Sir Mix-A-Lot have songs about it.")
    password = input()
    pw = ['Butts', 'butts', 'butt', 'Butt', 'ass', 'Ass']
    if password in pw:
            print("Accass Granted. Get it, like ass.")
    else: print("Access Denied.")
elif name == 'Taufiq':
    print('Das ghey')
else: print ("Hello there, " + name + "!")
