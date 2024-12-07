list_1 = []
list_2 = []
distance = 0

def read_input():
    with open("day1/input.txt", "r") as f:
        for line in f:
            s = line.split()
            list_1.append(s[0])
            list_2.append(s[1])
    list_1.sort()
    list_2.sort()

if __name__ == "__main__":
    read_input()

    for i in range(len(list_1)):
        distance += abs(int(list_1[i]) - int(list_2[i]))
    
    print(distance)
