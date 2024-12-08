number_of_safe_reports = 0
signs_between_levels = []

def report_is_safe(current_report):
    signs_between_levels.clear()
    for i in range(1, len(current_report)):
        difference = current_report[i - 1] - current_report[i]
        if abs(difference) > 3 or difference == 0:
            break

        if current_report[i] > current_report[i - 1]:
            signs_between_levels.append("+")
        else:
            signs_between_levels.append("-")

    if len(signs_between_levels) == 0:
        return False
    return signs_between_levels.count(signs_between_levels[0]) == len(current_report) - 1


if __name__ == "__main__":
       with open("day2/input.txt", "r") as f:
        for line in f:
            report = [int(x) for x in line.split()]
            if report_is_safe(report):
                number_of_safe_reports += 1
                continue
            for i in range(0, len(report)):
                report_copy = report.copy()
                del(report_copy[i])
                if report_is_safe(report_copy):
                    number_of_safe_reports += 1
                    break

        print(number_of_safe_reports)