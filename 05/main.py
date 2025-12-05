#
# Day 05
# Solution 1: 525
# Solution 2: 333892124923577
#

raw = open("input.txt").read()


def parse(raw):
    top, bot = raw.split("\n\n")
    table = []
    for line in top.splitlines():
        x, y = line.split("-")
        table.append(range(int(x), int(y) + 1))
    data = [int(x) for x in bot.splitlines()]
    return table, data


table, data = parse(raw)


def solution_1():
    total = 0
    for item in data:
        for rng in table:
            if item in rng:
                total += 1
                break
    print(total)


def solution_2():
    def try_merge(a, b):
        if a.start >= b.start and a.start <= b.stop:
            # a starts within b
            return range(b.start, max(a.stop, b.stop))
        if b.start >= a.start and b.start <= a.stop:
            # b starts within a
            return range(a.start, max(a.stop, b.stop))
        return None

    # combine overlapping ranges as much as possible
    ranges = list(table)
    for i in reversed(range(len(ranges))):
        for j in range(i):
            merged = try_merge(ranges[i], ranges[j])
            if merged is not None:
                ranges[j] = merged
                del ranges[i]
                break

    # count values in all non-overlapping ranges
    total = 0
    for rng in ranges:
        total += rng.stop - rng.start
    print(total)


solution_1()
solution_2()
