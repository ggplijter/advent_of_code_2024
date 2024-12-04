import re
from tools import fetch_input, fetch_assignment

# The specific day you want to retrieve input for
DAY = 3  # Replace with the day of the puzzle
YEAR = 2024  # Replace with the current year if needed

# Use the function
input_data = fetch_input(url=f"https://adventofcode.com/{YEAR}/day/{DAY}/input")
if input_data:

    # ex1
    pattern = r"mul\((\d+),(\d+)\)"  # Captures two numbers inside mul()
    matches = re.findall(pattern, input_data)
    results = [int(a) * int(b) for a, b in matches]  # Evaluate all matches
    print(sum(results))


fetch_assignment(url=f"https://adventofcode.com/{YEAR}/day/{DAY}")