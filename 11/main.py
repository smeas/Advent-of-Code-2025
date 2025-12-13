#
# Day 11
# Solution 1: 688
# Solution 2:
#

import sys
from dataclasses import dataclass
from typing import Self

raw = open(sys.argv[1]).read()


@dataclass
class Node:
    name: str
    edges: list[Self]


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
        node = Node(name, [])
        nodes[name] = node
        if name == "you":
            start = node
        elif name == "out":
            end = node

    # build graph
    for row in rows:
        name, outputs = row
        for output_name in outputs:
            nodes[name].edges.append(nodes[output_name])

    # depth first search
    stack = [start]
    total = 0
    while stack:
        node = stack.pop()
        if node == end:
            total += 1
        else:
            stack.extend(node.edges)

    print(total)


solution_1()
