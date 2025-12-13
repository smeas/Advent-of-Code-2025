#
# Day 08
# Solution 1: 352584
# Solution 2: 9617397716
#

import math
from dataclasses import dataclass
raw = open("input.txt").read()
data = [tuple(map(int, line.split(","))) for line in raw.splitlines()]


def distance(a, b):
    x, y, z = a[0] - b[0], a[1] - b[1], a[2] - b[2]
    return math.sqrt(x*x + y*y + z*z)


def find_bucket(buckets, point):
    for i, bucket in enumerate(buckets):
        if point in bucket:
            return i
    return -1


@dataclass
class Pair:
    pt_a: tuple[int, int, int]
    pt_b: tuple[int, int, int]
    dist: float


# generate list of pairs ordered by distance for speed
dist_pairs = []  # type: list[Pair]
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        a, b = data[i], data[j]
        dist_pairs.append(Pair(a, b, distance(a, b)))
dist_pairs.sort(key=lambda pair: pair.dist)

circuits = [[x] for x in data]


def solution_1():
    for _ in range(1000):
        pair = dist_pairs.pop(0)

        bucket_a = find_bucket(circuits, pair.pt_a)
        bucket_b = find_bucket(circuits, pair.pt_b)

        if bucket_a != bucket_b:
            circuits[bucket_a].extend(circuits[bucket_b])
            del circuits[bucket_b]

    for e in circuits:
        print(len(e), e)

    s = list(sorted((len(c) for c in circuits), reverse=True))
    print(s)
    print(s[0] * s[1] * s[2])


def general_solution():
    for i in range(len(dist_pairs)):
        pair = dist_pairs.pop(0)

        bucket_a = find_bucket(circuits, pair.pt_a)
        bucket_b = find_bucket(circuits, pair.pt_b)

        if bucket_a != bucket_b:
            circuits[bucket_a].extend(circuits[bucket_b])
            del circuits[bucket_b]

        if i == 999:  # 1000th iteration
            s = list(sorted((len(c) for c in circuits), reverse=True))
            print(s)
            print(s[0] * s[1] * s[2])  # solution 1

        if len(circuits) == 1:
            print(pair.pt_a[0] * pair.pt_b[0])  # solution 2
            break


# solution_1()
general_solution()
