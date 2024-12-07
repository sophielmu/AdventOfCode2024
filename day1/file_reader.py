list_1 = []
list_2 = []

def read_input():
    with open("day1/input.txt", "r") as f:
        for line in f:
            s = line.split()
            list_1.append(s[0])
            list_2.append(s[1])

    return (list_1, list_2)