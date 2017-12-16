from math import sqrt

number = int(input("Find the Pythagorean Triplet of: "))


def problem9(number):
  a, b, c = 0, 0, 0

  while True:
    if a + b + c == number and a < b and b < c:
      break
    a = 0
    b += 1

    while True:
      a += 1
      c = sqrt((a ** 2) + (b ** 2))
      if a + b + c == number:
        break
      if a > b:
        break
  return a, b, c


solved = problem9(number)
a = solved[0]
b = solved[1]
c = solved[2]

print("Found closest Pythagorean Triplet for", number, "\n the triplet was:", a, b, c, ".")
print("The product of:", a, ",", b, ",", "and", c, "is:", a * b * c)
