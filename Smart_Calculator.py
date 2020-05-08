# Stage 1

a = input().split(' ')
c = 0
for i in a:
    c += int(i)
print(c)


# Stage 2

while True:
    a = input()
    if a == "":
        continue
    elif a == "/exit":
        print("Bye!")
        break
    else:
        ls = [int(i) for i in a.split(" ")]
        print(int(sum(ls)))


# Stage 3

while True:
    a = input()
    if a == "":
        continue
    elif a == "/help":
        print("The program calculates the sum of numbers")
    elif a == "/exit":
        print("Bye!")
        break
    else:
        ls = [int(i) for i in a.split(" ")]
        print(int(sum(ls)))


# Stage 4

while True:
    a = input()
    if a == "":
        continue
    elif a == "/help":
        print("The program calculates the sum of numbers")
    elif a == "/exit":
        print("Bye!")
        break
    else:
        print(eval(a))


# Stage 5

while True:
    a = input()
    if a == "":
        continue
    elif a == "/help":
        print("The program calculates the sum of numbers")
    elif a == "/exit":
        print("Bye!")
        break
    else:
        try:
            print(eval(a))
        except SyntaxError:
            if a.startswith("/"):
                print("Unknown command")
            else:
                print("Invalid expression")
        except NameError:
            print("Invalid expression")
