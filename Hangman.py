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


# Stage 5

import random

print("H A N G M A N")
print()

wordlist = ['python', 'java', 'kotlin', 'javascript']
pattern = random.choice(wordlist)
random_word = list(pattern)
hyphens_num = list('-' * len(random_word))

hyphens_count = hyphens_num.count('-')

hyphens_join = ''.join(hyphens_num)

tries = 0
while tries < 8:

    tries += 1
    print(hyphens_join)
    a = input('Input a letter: ')

    i = random_word.count(a)
    if i == 0 and hyphens_num.count('-') > 0:
        print('No such letter in the word')
        print()

    else:
        while i != 0:
            b = random_word.index(a)
            hyphens_num[b] = a
            random_word[b] = '-'
            i -= 1
            hyphens_count = hyphens_num.count('-')
        hyphens_join = ''.join(hyphens_num)
        print()

print("""Thanks for playing!
We'll see how well you did in the next stage """)
