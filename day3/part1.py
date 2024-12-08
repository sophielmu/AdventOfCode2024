import re

total = 0

if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        matches = re.findall("mul\\(\\d+,\\d+\\)", f.read())
        for match in matches:
            numbers = re.findall("\\d+", match)
            total += int(numbers[0]) * int(numbers[1])
        print(total)