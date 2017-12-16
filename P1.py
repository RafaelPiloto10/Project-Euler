class Program:
    def __init__(self):
        self.max = 1000
        self.multi1 = 5
        self.multi2 = 3
        self.total = 0

        self.check()

    def check(self):
        for i in range(self.max):
            if i % self.multi1 == 0:
                self.total += i
            elif i % self.multi2 == 0:
                self.total += i

        print(self.total)

if __name__ == "__main__":
    program = Program()
