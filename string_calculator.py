import re


class stringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if len(numbers) == 1 and numbers.isdigit():
            return int(numbers)

        delimiter = ","

        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split(
                "\n", 1)  # get the delimiter and numbers
        else:
            numbers = re.sub(r"[\n]", delimiter, numbers)

        num_list = list(map(int, numbers.split(delimiter)))
        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError("Negatives not allowed: {}".format(
                ",".join(map(str, negatives))))

        return sum(num_list)
