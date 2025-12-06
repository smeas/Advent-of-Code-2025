#
# Day 06
# Solution 1: 5733696195703
# Solution 2: 10951882745757
#

import functools
import itertools
import operator

raw = open("input.txt").read()
ops = {
    "*": operator.mul,
    "+": operator.add,
}


def solution_1():
    data = [[s for s in line.split(" ") if s] for line in raw.splitlines()]
    data = [list(row) for row in zip(*data)]  # transpose

    total = 0
    for row in data:
        op = ops[row[-1]]
        total += functools.reduce(op, (int(val) for val in row[:-1]))

    print(total)


def solution_2():
    data = [list(row) for row in raw.splitlines()]
    data = [list(row) for row in itertools.zip_longest(
        *data, fillvalue=" ")]  # transpose
    row_size = len(data[0])

    total = 0
    current = []
    current_op = None
    for row in data:
        if row == [" "] * row_size:
            total += functools.reduce(current_op, current)
            current = []
            continue

        if row[-1] != " ":
            current_op = ops[row[-1]]

        s = ""
        for cell in row[:-1]:
            if cell != " ":
                s += cell

        current.append(int(s))

    total += functools.reduce(current_op, current)
    print(total)


solution_1()
solution_2()
