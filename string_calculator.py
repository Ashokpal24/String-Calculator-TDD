import re


class stringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if len(numbers) == 1 and numbers.isdigit():
            return int(numbers)

        delimiters = ","

        if numbers.startswith("//"):
            # check if delimiters start are in [] and get list of it
            delimiters = re.findall(r"\[(.*?)\]", numbers)

            if delimiters == []:
                # if list empty just get the delimiter (assuming only 1 delimiter exist without [])
                delimiters, numbers = numbers[2:].split("\n")
            else:
                # if multiple delimiter exists in [] add escape and join using OR
                numbers = numbers[2:].split("\n", 1)[1]
                delimiters = "|".join(map(re.escape, delimiters))
        else:
            numbers = re.sub(r"[\n]", delimiters, numbers)

        if not numbers:
            return 0

        num_list = map(int, re.split(delimiters, numbers))

        # check for number greater than 1000
        num_list = [n for n in num_list if n < 1001]

        # check for negatives
        negatives = [n for n in num_list if n < 0]

        if negatives:
            raise ValueError("Negatives not allowed: {}".format(
                ",".join(map(str, negatives))))

        return sum(num_list)
