def collatz(n):
  if n % 2 == 0:
    return n // 2
  else:
    return n * 3 + 1


def problem14(n):
  count = 1
  maxi = n
  length = 1
  heighLength = 0
  heighNum = 0

  while count <= maxi:
    calculating = True
    length = 0
    x = count
    length += 1

    while calculating:
      x = collatz(x)
      if x == 1:
        calculating = False

      if calculating:
        length += 1

    if length >= heighLength:
      heighLength = length
      heighNum = count

    length += 1
    count += 1
  return heighNum, heighLength


maximum = int(input("Enter the maximum number you would like to collaptz: "))

collaptzed = problem14(maximum)

print("Got results\nThe maximum number, whose vaule is under {} and produced the largest chain is {}. The chain length was {}".format(maximum, collaptzed[0], collaptzed[1]))
