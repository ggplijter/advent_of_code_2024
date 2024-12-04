from tools import fetch_input, fetch_assignment

# The specific day you want to retrieve input for
DAY = 1  # Replace with the day of the puzzle
YEAR = 2024  # Replace with the current year if needed

# Use the function
input_data = fetch_input(url=f"https://adventofcode.com/{YEAR}/day/{DAY}/input")



if input_data:
    print("Input retrieved successfully!")
    l1, l2 = zip(*[(int(x.split(" ")[0]), int(x.split(" ")[-1])) for x in  input_data.split("\n")])

    # ex 1
    distance = 0
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    for i in range(len(l1)):
        val1 = l1_sorted.pop(0)
        val2 = l2_sorted.pop(0)
        distance += abs(val1 - val2)
    print(f"Distance: {distance}")

    # ex 2
    similarity = 0
    for val in l1:
        occurences = sum([1 for x in l2 if x==val])
        similarity += occurences * val
    print(f"Similarity: {similarity}")

fetch_assignment(url=f"https://adventofcode.com/{YEAR}/day/{DAY}")