# write your code here

# Stage 1

print('''
Hello! My name is Aid.
I was created in 2020.''')


# Stage 2

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

yourName = input()
print(f'What a great name you have, {yourName}!')


# Stage 3

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
yourAge = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {yourAge}; that's a good time to start programming!")


# Stage 4

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

number = int(input())
for i in range(0, number + 1):
    print(i,"!")
print('Completed, have a nice day!')


# Stage 5

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        opt = int(input())
        if opt == 2:
            break
        else:
            print("Please, try again.")
    print('Completed, have a nice day!')

def end():
    print('Congratulations, have a nice day!')

greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
end()
