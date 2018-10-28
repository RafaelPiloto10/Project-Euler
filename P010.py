from math import sqrt
n = input("Enter a positive integer: ")

def problem10(n):
  total = 0
  i = 2
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
