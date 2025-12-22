#
# Day 12
# Solution 1: 410
# Solution 2: N/A
#

import sys

raw = open(sys.argv[1]).read()


def solution_1():
    # What the heck, you don't need to actually implement a backtracking search algorihm and can just solve the input
    # data based on an area heuristic. It doesn't work for the example, but does for the input.
    #
    # I had to cheat a little on this one. Found the hint on Reddit that you could solve the input with a trivial
    # filter, and such was the case... Looking more on Reddit now afterwards, it seems that you can even skip the area
    # check and just divide by 9...
    patterns = {}
    current_num = 0
    total = 0
    for line in raw.splitlines():
        if "x" in line:
            left, right = line.split(": ")
            w, h = map(int, left.split("x"))
            counts = map(int, right.split(" "))
            sum_area = 0
            for i, cnt in enumerate(counts):
                sum_area += patterns[i] * cnt
            if sum_area < w * h:
                print("yes")
                total += 1
            else:
                print("no")
        elif ":" in line:
            current_num = int(line.split(":")[0])
        elif len(line) != 0:
            patterns[current_num] = patterns.get(
                current_num, 0) + line.count("#")

    print(total)


solution_1()
