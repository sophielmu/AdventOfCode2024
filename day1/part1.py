list1 = []
list2 = []
distance = 0

def read_input():
    with open("day1/input.txt", "r") as f:
        for line in f:
            s = line.split()
            list1.append(s[0])
            list2.append(s[1])
    list1.sort()
    list2.sort()

if __name__ == "__main__":
    read_input()

    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    
    print(distance)
