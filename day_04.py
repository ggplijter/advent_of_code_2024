import re
from tools import fetch_input, fetch_assignment

# The specific day you want to retrieve input for
DAY = 4  # Replace with the day of the puzzle
YEAR = 2024  # Replace with the current year if needed

# Use the function
input_data = fetch_input(url=f"https://adventofcode.com/{YEAR}/day/{DAY}/input")


class ex1:
    WORD = "XMAS"
    LOOKUP_LEN = len(WORD) - 1

    @staticmethod
    def look_left_up(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y - c][x - c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_left_down(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y + c][x - c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_up(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y - c][x] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_left(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y][x - c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_down(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y + c][x] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_right(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y][x + c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_right_up(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y - c][x + c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def look_right_down(m, pos: tuple[int, int]):
        x, y = pos
        word = "".join([m[y + c][x + c] for c in range(ex1.LOOKUP_LEN + 1)])
        return 1 if word == ex1.WORD else 0

    @staticmethod
    def solve(m):
        max_y = len(m)
        max_x = len(m[0])
        count = 0
        for y in range(max_y):  # vertical
            for x in range(max_x):  # horizontal
                if m[y][x] == "X":
                    #  look left
                    if x - ex1.LOOKUP_LEN >= 0:
                        count += ex1.look_left(m, pos=(x, y))

                    #  look right
                    if x <= (max_x - 1) - ex1.LOOKUP_LEN:
                        count += ex1.look_right(m, pos=(x, y))

                    # look up
                    if y - ex1.LOOKUP_LEN >= 0:
                        count += ex1.look_up(m, pos=(x, y))

                    #  look down
                    if y <= (max_y - 1) - ex1.LOOKUP_LEN:
                        count += ex1.look_down(m, pos=(x, y))

                    # look leftup
                    if (x - ex1.LOOKUP_LEN >= 0) and (y - ex1.LOOKUP_LEN >= 0):
                        count += ex1.look_left_up(m, pos=(x, y))

                    # look leftdown
                    if (x - ex1.LOOKUP_LEN >= 0) and (
                        y <= (max_y - 1) - ex1.LOOKUP_LEN
                    ):
                        count += ex1.look_left_down(m, pos=(x, y))

                    # look rightup:
                    if (x <= (max_x - 1) - ex1.LOOKUP_LEN) and (
                        y - ex1.LOOKUP_LEN >= 0
                    ):
                        count += ex1.look_right_up(m, pos=(x, y))

                    # look rightdown:
                    if (x <= (max_x - 1) - ex1.LOOKUP_LEN) and (
                        y <= (max_y - 1) - ex1.LOOKUP_LEN
                    ):
                        count += ex1.look_right_down(m, pos=(x, y))

        print(f"Found {count} times the word {ex1.WORD}")


class ex2:
    WORD = "MAS"
    LOOKUP_LEN = 1

    @staticmethod
    def check_for_x_mas(m, pos: tuple[int, int]):
        x, y = pos

        # first from bottom-left to up-right
        word_bleft_uright = "".join(
            [m[y + 1 - c][x - 1 + c] for c in range(ex2.LOOKUP_LEN + 2)]
        )
        word_uleft_dright = "".join(
            [m[y - 1 + c][x - 1 + c] for c in range(ex2.LOOKUP_LEN + 2)]
        )

        return (
            1
            if (word_bleft_uright == ex2.WORD and word_uleft_dright == ex2.WORD)
            or (
                word_bleft_uright == ex2.WORD[::-1]
                and word_uleft_dright == ex2.WORD[::-1]
            )
            or (
                       word_bleft_uright == ex2.WORD
                       and word_uleft_dright == ex2.WORD[::-1]
               )
               or (
                       word_bleft_uright == ex2.WORD[::-1]
                       and word_uleft_dright == ex2.WORD
               )
            else 0
        )

    @staticmethod
    def solve(m):
        max_y = len(m)
        max_x = len(m[0])
        count = 0
        for y in range(max_y):  # vertical
            for x in range(max_x):  # horizontal
                if m[y][x] == "A":
                    if 1 <= x < max_x - 1 and 1 <= y < max_y - 1:
                        count += ex2.check_for_x_mas(m, pos=(x, y))

        print(f"Found {count} times the word {ex2.WORD} crossed")


if input_data:
    # print(input_data)
    matrix = [[c for c in row] for row in input_data.split("\n")]

    ex1.solve(m=matrix)
    ex2.solve(m=matrix)


fetch_assignment(url=f"https://adventofcode.com/{YEAR}/day/{DAY}")
