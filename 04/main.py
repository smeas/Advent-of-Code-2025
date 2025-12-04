#
# Day 04
# Solution 1: 1478
# Solution 2: 9120
#

data = [[col for col in line.strip()] for line in open("input.txt").readlines()]

def solution_1():
	total = 0
	size_y = len(data)
	size_x = len(data[0])

	def check_coord(x, y):
		if x < 0 or y < 0 or x > size_x - 1 or y > size_y - 1:
			return 0
		return 1 if data[y][x] == "@" else 0

	def can_remove(x, y):
		num = 0
		num += check_coord(x + -1, y + -1)
		num += check_coord(x + -1, y + 0)
		num += check_coord(x + -1, y + 1)
		num += check_coord(x + 0, y + -1)
		num += check_coord(x + 0, y + 1)
		num += check_coord(x + 1, y + -1)
		num += check_coord(x + 1, y + 0)
		num += check_coord(x + 1, y + 1)
		return num < 4

	for y in range(size_y):
		for x in range(size_x):
			if data[y][x] != "@":
				continue

			if can_remove(x, y):
				total += 1

	print(total)

def solution_2():
	total = 0
	size_y = len(data)
	size_x = len(data[0])

	def check_coord(x, y):
		if x < 0 or y < 0 or x > size_x - 1 or y > size_y - 1:
			return 0
		return 1 if data[y][x] == "@" else 0

	def can_remove(x, y):
		num = 0
		num += check_coord(x + -1, y + -1)
		num += check_coord(x + -1, y + 0)
		num += check_coord(x + -1, y + 1)
		num += check_coord(x + 0, y + -1)
		num += check_coord(x + 0, y + 1)
		num += check_coord(x + 1, y + -1)
		num += check_coord(x + 1, y + 0)
		num += check_coord(x + 1, y + 1)
		return num < 4

	while True:
		removed_this_time = 0
		for y in range(size_y):
			for x in range(size_x):
				if data[y][x] == "@" and can_remove(x, y):
					data[y][x] = "x"
					removed_this_time += 1
					total += 1

		if removed_this_time == 0:
			break

	print(total)


solution_1()
solution_2()
