import re

total = 0
matches = []
mul_string_regex = "mul\\(\\d+,\\d+\\)"

if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        input_text = f.read()
        first_string = re.search(".+?(?=don't\(\))", input_text).string
        # last_string = re.search(".+?(?=don't\(\))") # todo something
        matches = re.findall(mul_string_regex, first_string)
        cleansed_input = input_text.removeprefix(first_string)
        do_dont_strings = re.findall("do\(\).+?(?=don't\(\))", cleansed_input)

        for string in do_dont_strings:
            matches.append(re.findall(mul_string_regex, f.read()))

        for match in matches:
            numbers = re.findall("\\d+", match)
            total += int(numbers[0]) * int(numbers[1])

        print(total)