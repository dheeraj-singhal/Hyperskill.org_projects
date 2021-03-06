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


# Stage 6

import random

print("H A N G M A N")

wordlist = ['python', 'java', 'kotlin', 'javascript']
pattern = random.choice(wordlist)
random_word = list(pattern)
hyphens_num = list('-' * len(random_word))

hyphens_count = hyphens_num.count("-")
hyphens_join = ''.join(hyphens_num)

tries = 8
selected = set()

while hyphens_count > 0 and tries > 0:
    print()
    print(hyphens_join)
    guess = input("Input the letter: ")
    if guess in pattern and guess not in selected:
        for i in range(len(pattern)):
            if guess == pattern[i]:
                hyphens_num[i] = pattern[i]
                hyphens_count -= 1
                if guess not in selected:
                    selected.add(guess)

    elif guess in selected:
        tries -= 1
        if tries >= 0:
            print("No improvements")

    elif tries > 0 and guess not in pattern:
        print("No such letter in the word")
        tries -= 1
    hyphens_join = "".join(hyphens_num)

if tries != 0 and hyphens_count == 0:
        print(pattern)
        print("You guessed the word!")
        print("You survived!")
elif tries == 0 and hyphens_count == 0:
        print(pattern)
        print("You guessed the word!")
        print("You survived!")
else:
        print("You are hanged!")


# Stage 7

import random

print("H A N G M A N")

wordlist = ['python', 'java', 'kotlin', 'javascript']
pattern = random.choice(wordlist)
random_word = list(pattern)
hyphens_num = list('-' * len(random_word))

hyphens_count = hyphens_num.count("-")
hyphens_join = ''.join(hyphens_num)

tries = 8
selected = set()

while hyphens_count > 0 and tries > 0:
    print()
    print(hyphens_join)
    guess = input("Input the letter: ")
    if len(guess) == 1 and guess.isalpha() and guess.islower():
        if guess in pattern and guess not in selected:
            for i in range(len(pattern)):
                if guess == pattern[i]:
                    hyphens_num[i] = pattern[i]
                    hyphens_count -= 1
                    if guess not in selected:
                        selected.add(guess)

        elif guess in selected:

            if tries >= 0:
                print("You already typed this letter")

        elif tries > 0 and guess not in pattern:
            print("No such letter in the word")
            tries -= 1
            if guess not in selected:
                selected.add(guess)
        hyphens_join = "".join(hyphens_num)
    elif len(guess) > 1:
        print("You should print a single letter")
    else:
        print("It is not an ASCII lowercase letter")

if tries != 0 and hyphens_count == 0:
    print(pattern)
    print("You guessed the word!")
    print("You survived!")
elif tries == 0 and hyphens_count == 0:
    print(pattern)
    print("You guessed the word!")
    print("You survived!")
else:
    print("You are hanged!")


# Stage 8

import random

print("H A N G M A N")
while input('Type "play" to play the game, "exit" to quit:') == "play":
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    pattern = random.choice(wordlist)
    random_word = list(pattern)
    hyphens_num = list('-' * len(random_word))

    hyphens_count = hyphens_num.count("-")
    hyphens_join = ''.join(hyphens_num)

    tries = 8
    selected = set()

    while hyphens_count > 0 and tries > 0:
        print()
        print(hyphens_join)
        guess = input("Input the letter: ")
        if len(guess) == 1 and guess.isalpha() and guess.islower():
            if guess in pattern and guess not in selected:
                for i in range(len(pattern)):
                    if guess == pattern[i]:
                        hyphens_num[i] = pattern[i]
                        hyphens_count -= 1
                        if guess not in selected:
                            selected.add(guess)

            elif guess in selected:

                if tries >= 0:
                    print("You already typed this letter")

            elif tries > 0 and guess not in pattern:
                print("No such letter in the word")
                tries -= 1
                if guess not in selected:
                    selected.add(guess)
            hyphens_join = "".join(hyphens_num)
        elif len(guess) > 1:
            print("You should print a single letter")
        else:
            print("It is not an ASCII lowercase letter")

    if tries != 0 and hyphens_count == 0:
        print(pattern)
        print("You guessed the word!")
        print("You survived!")
    elif tries == 0 and hyphens_count == 0:
        print(pattern)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")