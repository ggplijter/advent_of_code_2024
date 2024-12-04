import re
from tools import fetch_input, fetch_assignment

# The specific day you want to retrieve input for
DAY = 3  # Replace with the day of the puzzle
YEAR = 2024  # Replace with the current year if needed

# Use the function
input_data = fetch_input(url=f"https://adventofcode.com/{YEAR}/day/{DAY}/input")
if input_data:

    # ex1
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_data)
    results = [int(a) * int(b) for a, b in matches]  # Evaluate all matches
    print(sum(results))

    pattern = r"\bdo\(\)|\bmul\(\d+,\d+\)|\bdon't\(\)"
    # pattern = r"\bdon't\(\)|\bmul\(\d+,\d+\)|\bdo\(\)"
    matches = re.findall(pattern, input_data)

    do_sumup = True
    counter = 0
    for m in matches:
        if m == "do()":
            do_sumup = True
            continue

        if m == "don't()":
            do_sumup = False
            continue


        if do_sumup:
            num0, num1 = re.findall(r"mul\((\d+),(\d+)\)", m).pop(0)
            counter += int(num0) * int(num1)
    print(counter)



    
# fetch_assignment(url=f"https://adventofcode.com/{YEAR}/day/{DAY}")