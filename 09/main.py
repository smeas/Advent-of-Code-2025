#
# Day 08
# Solution 1: 4771508457
# Solution 2: 1539809693
#

from itertools import groupby, pairwise, chain
from math import copysign

raw = open("input.txt").read()
data = [tuple(map(int, line.split(","))) for line in raw.splitlines()]


def area(a, b):
    return (1+abs(a[0] - b[0])) * (1+abs(a[1] - b[1]))


def solution_1():
    max_area = 0

    for a in data:
        for b in data:
            if a == b:
                continue
            new_area = area(a, b)
            if new_area > max_area:
                max_area = new_area

    print(max_area)


class Point:
    pos: tuple[int, int]
    compact_pos: tuple[int, int]

    def __init__(self, point):
        self.pos = point
        self.compact_pos = (0, 0)

    def __repr__(self):
        return f"({self.pos}|{self.compact_pos})"


def solution_2():
    #
    # solve the puzzle visually by performing the rectangle validity checks on a rasterized compacted version of the grid
    #
    points = list(map(Point, data))

    # calculate the compact version of the grid
    def x_pos_key(pt): return pt.pos[0]
    def y_pos_key(pt): return pt.pos[1]
    current_col = 0
    for key, grp in groupby(sorted(points, key=x_pos_key), key=x_pos_key):
        for point in grp:
            point.compact_pos = (current_col, 0)
        current_col += 1
    current_row = 0
    for key, grp in groupby(sorted(points, key=y_pos_key), key=y_pos_key):
        for point in grp:
            col, _ = point.compact_pos
            point.compact_pos = (col, current_row)
        current_row += 1

    # create visual grid map
    max_x = max(points, key=lambda pt: pt.compact_pos[0]).compact_pos[0] + 1
    max_y = max(points, key=lambda pt: pt.compact_pos[1]).compact_pos[1] + 1
    grid = []
    for i in range(max_y):
        grid.append(['.'] * max_x)

    # rasterize points
    for point in points:
        x, y = point.compact_pos
        grid[y][x] = '#'

    # rasterize edges
    for p1, p2 in pairwise(chain(points, [points[0]])):
        if p1.compact_pos[0] == p2.compact_pos[0]:
            dx, dy = 0, int(copysign(1, p2.compact_pos[1] - p1.compact_pos[1]))
        else:
            assert p1.compact_pos[1] == p2.compact_pos[1]
            dx, dy = int(copysign(1, p2.compact_pos[0] - p1.compact_pos[0])), 0

        px, py = p1.compact_pos[0], p1.compact_pos[1]
        while True:
            px += dx
            py += dy
            if px == p2.compact_pos[0] and py == p2.compact_pos[1]:
                break
            grid[py][px] = 'x'

    # find a point on the inside
    seed = None
    for y in range(len(grid)):
        transitions = 0
        last_was_edge = False
        candidate_seed = None
        for x in range(len(grid[0])):
            is_edge = grid[y][x] != '.'
            if last_was_edge != is_edge:
                transitions += 1
                last_was_edge = is_edge
                if transitions == 2:
                    assert not is_edge
                    candidate_seed = (x, y)

        if transitions > 2:
            seed = candidate_seed
            break

    assert seed, "seed not found"

    # flood fill inner area
    def flood_fill(grid, seed):
        w, h = len(grid[0]), len(grid)
        stack = [seed]
        while stack:
            x, y = stack.pop()
            if 0 <= x < w and 0 <= y < h and grid[y][x] == '.':
                grid[y][x] = 'x'
                stack.append((x - 1, y))
                stack.append((x, y - 1))
                stack.append((x + 1, y))
                stack.append((x, y + 1))

    flood_fill(grid, seed)

    # find maximum valid area
    def is_valid_area(point_a: Point, point_b: Point):
        min_x = min(point_a.compact_pos[0], point_b.compact_pos[0])
        max_x = max(point_a.compact_pos[0], point_b.compact_pos[0])
        min_y = min(point_a.compact_pos[1], point_b.compact_pos[1])
        max_y = max(point_a.compact_pos[1], point_b.compact_pos[1])
        # check left and right edges
        for y in range(min_y, max_y + 1):
            if grid[y][min_x] == '.' or grid[y][max_x] == '.':
                return False
        # check top and bottom edges
        for x in range(min_x, max_x + 1):
            if grid[min_y][x] == '.' or grid[max_y][x] == '.':
                return False

        return True

    max_area = 0
    for a in points:
        for b in points:
            if a == b or not is_valid_area(a, b):
                continue
            new_area = area(a.pos, b.pos)
            if new_area > max_area:
                max_area = new_area

    print(max_area)


solution_1()
solution_2()
