def problem20(start):
    a, b, c = [i for i in range(1, start)], 1, 0
    for i in a:
        b = b * i
    for i in str(b):
        c += int(i)
    return c


startPoint = input("This program calculates the factorial sum of a number.\nEnter the number you would like to calculate: ")
solve = problem20(int(startPoint))
print("The factorial sum of the number", startPoint, "is", solve, ".")
