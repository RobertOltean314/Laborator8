from Calculator import Calculator


class AdvancedCalculator(Calculator):
    def __init__(self, value: float):
        super().__init__(value)

    def sqrt(self):
        self.value = self.value ** 0.5
