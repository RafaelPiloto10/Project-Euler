def Problem(n):  
  counter = 0
  for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
      counter += i
      
  return counter

print("Count the sum of all of the numbers divisible by 3 or 5 below: "), print(":", Problem(int(input())), " - Sum")

