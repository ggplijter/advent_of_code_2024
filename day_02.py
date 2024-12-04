import copy

from tools import fetch_input, fetch_assignment

# The specific day you want to retrieve input for
DAY = 2  # Replace with the day of the puzzle
YEAR = 2024  # Replace with the current year if needed


def diff(l: list):
    n = len(l)
    d = []
    for i in range(n - 1):
        d.append(l[i + 1] - l[i])
    return d

# Use the function
input_data = fetch_input(url=f"https://adventofcode.com/{YEAR}/day/{DAY}/input")
if input_data:
    data = [[int(l) for l in x.split(" ")] for x in input_data.split("\n")]

    # ex 1
    data_diff = [diff(d) for d in data]
    check_safe_reports = [
        1
        for diff_d in [diff(d) for d in data]
        if (all(x > 0 for x in diff_d) or all(x < 0 for x in diff_d)) and all(0 < abs(x) < 4 for x in diff_d)
    ]
    print(f"amount of safe reports: {len(check_safe_reports)} ")

    # ex 2
    unsafe_reports = [
        (
            None
            if (all(x > 0 for x in diff(d)) or all(x < 0 for x in diff(d))) and all(0 < abs(x) < 4 for x in diff(d))
            else d
        )
        for d in data
    ]

    count = 0
    for report in unsafe_reports:
        if report:
            already_deleted = False
            for i in range(len(report)):
                if already_deleted:
                    break
                tmp_report = copy.copy(report)
                tmp_report.pop(i)
                if (all(x > 0 for x in diff(tmp_report)) or all(x < 0 for x in diff(tmp_report))) and all(
                    0 < abs(x) < 4 for x in diff(tmp_report)
                ):
                    print(f"{report=} is still valid by deleting {i=} {diff(tmp_report)=}  ")
                    already_deleted = True
                    count += 1

    print(f"amount of safe reports by applying the 'Problem Dampener' : {len(check_safe_reports) + count} ")

fetch_assignment(url=f"https://adventofcode.com/{YEAR}/day/{DAY}")