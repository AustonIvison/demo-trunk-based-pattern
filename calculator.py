class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == "__main__":
    calc = Calculator()
    print("1 + 2 =", calc.add(1, 2))
