#
# Day 01
# Solution 1: 1141
# Solution 2: 6634
#

from math import trunc

data = open("input.txt").readlines()

def solution_1():
	dial = 50
	zero_counter = 0
	for line in data:
		dir = 1 if line[0] == 'R' else -1
		num = int(line[1:])
		dial += (num * dir)
		dial %= 100 # python has the "good" modulus for this use case
		if dial == 0:
			zero_counter += 1

	print(dial, zero_counter)

def solution_2():
	dial = 50
	zero_counter = 0
	for line in data:
		dir = 1 if line[0] == 'R' else -1
		num = int(line[1:])

		# first see if we even reach zero once
		dist_to_zero = (100 - dial) if (dial != 0 and dir == 1) else (dial)
		reaches_zero = dial != 0 and dist_to_zero <= num
		if reaches_zero:
			zero_counter += 1
		# then check for how many times we pass zero after that by counting the number of full turns
		num_full_rotations = trunc((num - dist_to_zero) / 100)
		zero_counter += num_full_rotations

		dial += (num * dir)
		dial %= 100 # python has the "good" modulus for this use case

	print(dial, zero_counter)

solution_1()
solution_2()
