class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def power(self, a, b):
        # Feature flagged
        import json
        with open('flags.json', 'r') as f:
            flags = json.load(f)
        if flags.get('new_power_feature', False):
            return a ** b
        else:
            raise NotImplementedError("Feature not enabled")

    def modulus(self, a, b):
        # Feature flagged
        import json
        with open('flags.json', 'r') as f:
            flags = json.load(f)
        if flags.get('new_modulus_feature', False):
            return a % b
        else:
            raise NotImplementedError("Feature not enabled")

if __name__ == "__main__":
    calc = Calculator()
    print("1 + 2 =", calc.add(1, 2))
