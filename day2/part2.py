number_of_safe_reports = 0

def 




if __name__ == "__main__":
       with open("day2/input.txt", "r") as f:
        for line in f:
            report = [int(x) for x in line.split()]

            for i in range(1, len(report)):
                difference = report[i - 1] - report[i]
                if abs(difference) > 3 or difference == 0:
                    del report[i]




            # iterate the safe reports here if we're good

        print(number_of_safe_reports)