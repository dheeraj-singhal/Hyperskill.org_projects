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
