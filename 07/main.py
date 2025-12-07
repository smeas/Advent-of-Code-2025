#
# Day 07
# Solution 1: 1524
# Solution 2: 32982105837605
#

raw = open("input.txt").read().splitlines()


def solution_1():
    total = 0
    data = [list(row) for row in raw]  # clone data
    for row_index, row in enumerate(data):
        for i, chr in enumerate(row):
            if data[row_index - 1][i] in ("S", "|"):
                if chr == ".":
                    row[i] = "|"
                elif chr == "^":
                    row[i-1] = "|"
                    row[i+1] = "|"
                    total += 1

    print(total)


def general_solution():
    num_splits = 0
    data = [list(row) for row in raw]  # clone data

    def increment(row, i, amt):
        if type(row[i]) is int:
            row[i] += amt
        else:
            row[i] = amt

    for row_index, row in enumerate(data[1:], start=1):
        for col_index, chr in enumerate(row):
            source = data[row_index - 1][col_index]
            if source in (".", "^"):
                continue

            if source == "S":
                source = 1

            if chr == "^":
                increment(row, col_index - 1, source)
                increment(row, col_index + 1, source)
                num_splits += 1
            else:
                increment(row, col_index, source)

    print(num_splits)  # solution 1
    # count beams that reached the bottom row
    print(sum(filter(lambda x: type(x) is int, data[-1])))  # solution 2


# solution_1()
general_solution()
