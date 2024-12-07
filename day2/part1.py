number_of_safe_reports = 0

if __name__ == "__main__":
       with open("day2/input.txt", "r") as f:
        for line in f:
            report = [int(x) for x in line.split()]
            signs_between_levels = []

            for i in range(1, len(report)):
                difference = report[i - 1] - report[i]
                if abs(difference) > 3 or difference == 0:
                    break

                if report[i] > report[i - 1]:
                    signs_between_levels.append("+")
                else:
                    signs_between_levels.append("-")

            if len(signs_between_levels) == 0:
                continue
            all_signs_are_the_same = signs_between_levels.count(signs_between_levels[0]) == len(report) - 1
            if all_signs_are_the_same:
                number_of_safe_reports += 1

        print(number_of_safe_reports)



