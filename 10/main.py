#
# Day 10
# Solution 1: 449
# Solution 2:
#

raw = open("input.txt").read()


def solution_1():
    total = 0
    for line in raw.splitlines():
        # parse goal and buttons as bitsets stored as int
        goal = sum(1 << i for i, c in enumerate(
            line[1:line.index("]")]) if c == "#")
        button_str = line[line.index("("):line.rindex(")") + 1]
        buttons = [
            sum(1 << int(i) for i in group[1:-1].split(",")) for group in button_str.split(" ")]

        # compute while deduplicating
        current_set = {0}
        presses = 0
        while True:
            presses += 1
            # compute all possible state permutations after this round of presses
            current_set = set(
                state ^ button for button in buttons for state in current_set)
            if goal in current_set:
                break

        total += presses

    print(total)


solution_1()
