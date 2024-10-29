class stringCalculator:
    def add(self, numbers: str) -> int:
        if len(numbers) == 1 and numbers.isdigit():
            return int(numbers)
        return 0
