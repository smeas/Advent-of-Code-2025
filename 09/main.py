#
# Day 08
# Solution 1: 4771508457
# Solution 2:
#


raw = open("input.txt").read()

data = [tuple(map(int, line.split(","))) for line in raw.splitlines()]

def area(a, b):
    return abs((a[0] - b[0] + 1) * (a[1] - b[1] + 1))

max_area = 0
max_a = None
max_b = None

for a in data:
    for b in data:
        if a == b:
            continue
        new_area = area(a, b)
        if new_area > max_area:
            print(new_area, a, b)
            max_area = new_area
            max_a = a
            max_b = b

print(max_area)
