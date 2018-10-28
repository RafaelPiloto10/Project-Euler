from math import sqrt
n = 10001

def problem7(n):
    last = []
    i = 2
    while i < n:
        p = True
        j = 2
        while j < sqrt(i) and p:
            if i % j == 0:
                p = False
            j += 1

        if p == True:
            last.append(i)

        i += 1
    return last

solve = problem7(n)

print(solve)
