from math import sqrt
n = input("Enter a positive integer: ")

def problem7(n):
  i = 2
  while i < n:
    p = True
    j = 2
    
    while j < sqrt(i) and p:
      if i % j == 0:
        p = False
      j += 1
      
    if p == True:
      last = i
      
    i += 1
  return last

solve = problem7(int(n))

print(solve)
