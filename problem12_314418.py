from math import sqrt

divisors = []
triangleNumbers = []
n = input("Enter a positive integer: ")



def problem12(n):
    for i in range(n):
      total = 0
      for x in range(i):
        total += x + 1
        if total not in triangleNumbers:
          triangleNumbers.append(total)
      
    total = 0
    i = 2
    for each in triangle
    while i < n:
        p = True
        j = 2
        
        while j <= sqrt(i) and p:
            if i % j == 0:
                p = False
            j += 1
          
        if p == True:
          total += i
          
        i += 1
      
      return total
      

    solve = problem10(int(n))

print("The sum of all of the prime numbers in the number:", n, "is", solve, ".")
