import re

total = 0
matches = []
mul_string_regex = "mul\\(\\d+,\\d+\\)"

if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        input_text = "do()" + f.read()
        input_text = input_text + "don't()"
        do_dont_strings = re.findall("do\(\).+?(?=don't\(\))", input_text)

        for string in do_dont_strings:
            string_match = re.findall(mul_string_regex, string)
            for mul_match in string_match:
                matches.append(mul_match)

        for match in matches:
            numbers = re.findall("\\d+", match)
            total += int(numbers[0]) * int(numbers[1])

        print(total)