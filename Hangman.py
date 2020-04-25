# Stage 1

print('''H A N G M A N
The game will be available soon.''')


# Stage 2

print('H A N G M A N')
name = input("Guess the word:")
if name == "python":
    print("You survived!")
else:
    print("You are hanged!")


# Stage 3

import random
language = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
name = input("Guess the word:")
if name == random.choice(language):
    print("You survived!")
else:
    print("You are hanged!")