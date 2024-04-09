class Calculator:
    def __init__(self, value: float):
        self.value = value

    def add(self, value: float):
        self.value += value

    def multiply(self, value: float):
        self.value *= value

    def divide(self, value: float):
        if value == 0:
            raise ValueError("Cannot divide by zero")
        else:
            self.value /= value

    def getResult(self):
        return self.value
