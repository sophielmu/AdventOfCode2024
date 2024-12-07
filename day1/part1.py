from day1.file_reader import read_input

distance = 0

if __name__ == "__main__":
    list_1, list_2 = read_input()

    list_1.sort()
    list_2.sort()
    
    for i in range(len(list_1)):
        distance += abs(int(list_1[i]) - int(list_2[i]))
    
    print(distance)
