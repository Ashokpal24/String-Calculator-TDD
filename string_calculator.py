class stringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if len(numbers) == 1 and numbers.isdigit():
            return int(numbers)

        num_list = map(int, numbers.split(","))
        return sum(num_list)
