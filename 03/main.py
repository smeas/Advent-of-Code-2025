#
# Day 03
# Solution 1: 17330
# Solution 2: 171518260283767
#

data = open("input.txt").readlines()

def solution_1():
	total = 0
	for line in data:
		line = line.strip()

		first = max(line[:-1], key=ord)
		first_index = line.index(first)
		second = max(line[first_index + 1:], key=ord)
		num = int(first + second)

		print(first, second, num)
		total += num

	print(total)

def general_solution(NUM_DIGITS):
	total = 0
	for line in data:
		line = line.strip()

		last_index = -1
		solution = ""
		for i in range(NUM_DIGITS):
			begin = last_index + 1
			end = len(line) - (NUM_DIGITS - 1) + len(solution)
			substr = line[begin:end]
			digit = max(substr, key=ord)
			last_index = begin + substr.index(digit)
			solution += digit
			#print(begin, end, substr, digit)

		num = int(solution)
		#print(num)
		total += num

	print(total)


general_solution(2)
general_solution(12)
