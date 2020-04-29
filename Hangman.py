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


# Stage 4

import random
language = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
hidden = random.choice(language)
name = input(f"Guess the word {hidden[0:3]+'-'*(len(hidden)-3)}:")
if name == hidden:
    print("You survived!")
else:
    print("You are hanged!")