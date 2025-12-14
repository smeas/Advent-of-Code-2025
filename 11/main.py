#
# Day 11
# Solution 1: 688
# Solution 2: 293263494406608
#

from functools import cache
from typing import Self

raw = open("input.txt").read()


class Node:
    name: str
    down: list[Self]

    def __init__(self, name):
        self.name = name
        self.down = []

    def __repr__(self):
        def name_key(x):
            return x.name
        return f"{self.name} -> ({", ".join(map(name_key, self.down))})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, value):
        return self.name == value.name


def solution_1():
    names = set()
    rows = []
    for line in raw.splitlines():
        print(line)
        key, right = line.split(": ")
        outputs = right.split(" ")
        rows.append((key, outputs))
        names.add(key)
        names.update(outputs)
    print(names)

    # create all nodes first
    nodes = {}  # type:dict[str, Node]
    start = None
    end = None
    for name in names:
        node = Node(name)
        nodes[name] = node
        if name == "you":
            start = node
        elif name == "out":
            end = node

    # build graph
    for row in rows:
        name, outputs = row
        for output_name in outputs:
            nodes[name].down.append(nodes[output_name])

    # depth first search
    stack = [start]
    total = 0
    while stack:
        node = stack.pop()
        if node == end:
            total += 1
        else:
            stack.extend(node.down)

    print(total)


def general_solution():
    names = set()
    rows = []
    for line in raw.splitlines():
        key, right = line.split(": ")
        outputs = right.split(" ")
        rows.append((key, outputs))
        names.add(key)
        names.update(outputs)

    # create all nodes first
    nodes = {}  # type:dict[str, Node]
    for name in names:
        node = Node(name)
        nodes[name] = node

    # build graph
    for row in rows:
        name, outputs = row
        for output_name in outputs:
            nodes[name].down.append(nodes[output_name])

    @cache  # memoize
    def path_count(start, end):
        if start == end:
            return 1
        return sum(path_count(other, end) for other in start.down)

    you = nodes["you"]
    svr = nodes["svr"]
    end = nodes["out"]
    dac = nodes["dac"]
    fft = nodes["fft"]

    print(path_count(you, end))  # solution 1

    # solution 2
    #
    # count paths from S to E passing through both A and B
    #
    # solution can be broken down into parts:
    #     count(S, A) * count(A, B) * count(B, E) +
    #     count(S, B) * count(B, A) * count(A, E)
    print(path_count(svr, fft) * path_count(fft, dac) * path_count(dac, end) +
          path_count(svr, dac) * path_count(dac, fft) * path_count(fft, end))

    # print(path_count.cache_info())


# solution_1()
general_solution()
