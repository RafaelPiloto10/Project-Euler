from math import sqrt

def getStart():
  x = input("What would you like to start at? If you would like to start with 1, simply press enter. Otherwise enter your value: ")
  try:
    int(x)
  except:
    return 1
  else:
    return int(sqrt(int(x)))
    
start = getStart()
x = int(input("What is the highest divisible number you would like to test: "))

global numbers
numbers = [i for i in range(1, x+1)]

def isDivisible(n):
  global numbers
  for i in numbers:
    if n % i == 0:
      pass
    else:
      return False
  return True

while True:
  Divisible = isDivisible(start)
      
  if Divisible:
    break
  else:
    start += 1
      
print("The smallest number divisible by", x, "was", start)
