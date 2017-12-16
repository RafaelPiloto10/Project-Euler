""" Project Euler Problem 2
Add up all of the Fibonacci numbers which are even
"""
class main:
    def __init__(self):
        self.max = 4000000
        self.counter = 0
        self.total = 0
        self.last = 1
        self.now = 2
        self.next = 0

        self.calculate()

    def calculate(self):
        while self.now < self.max:
            if self.now % 2 == 0:
                self.total += self.now

            self.next = self.now + self.last
            self.last = self.now
            self.now = self.next

            self.counter += 1
        print(self.total)

if __name__ == '__main__':
    main = main()
