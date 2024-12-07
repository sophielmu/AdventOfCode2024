list_1 = []
list_2 = []
similarity_score = 0

def read_input():
    with open("day1/input.txt", "r") as f:
        for line in f:
            s = line.split()
            list_1.append(s[0])
            list_2.append(s[1])

if __name__ == "__main__":
    read_input()

    for x in list_1:
        list_2_Occurences = list_2.count(x)
        similarity_score += int(x) * list_2_Occurences
    print(similarity_score)

