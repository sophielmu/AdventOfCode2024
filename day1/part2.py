from day1.file_reader import read_input

similarity_score = 0

if __name__ == "__main__":
    list_1, list_2 = read_input()

    for x in list_1:
        list_2_Occurences = list_2.count(x)
        similarity_score += int(x) * list_2_Occurences
    print(similarity_score)

