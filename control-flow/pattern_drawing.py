numbers = int(input("Enter the size of the pattern: "))
num = numbers
cons = numbers

while numbers > 0:
    while num > 0:
        print("*", end="")
        num = num - 1
    numbers = numbers - 1
    num = cons
    print("")

