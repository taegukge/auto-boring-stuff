import random

print('What would you like answered?')

ask = input()

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(ask + '\n' + messages[random.randint(0, len(messages) - 1)])
