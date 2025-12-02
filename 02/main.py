#
# Day 02
# Solution 1: 19605500130
# Solution 2: 36862281418
#

raw_data = open("input.txt").read()

def parse_range(s):
	a, b = s.split("-")
	return (int(a), int(b))

ranges = [parse_range(x) for x in raw_data.split(",")]

def solution_1():
	total = 0
	for a, b in ranges:
		for i in range(a, b + 1):
			s = str(i)
			mid = len(s) // 2
			if len(s) % 2 == 0 and s[0:mid] == s[mid:]:
				total += i

	print(total)

def solution_2():
	total = 0

	def check_invalid(num):
		s = str(num)
		max_rep_size = len(s) // 2
		for rep_size in range(1, max_rep_size + 1):
			if len(s) % rep_size != 0:
				continue

			check = s[0:rep_size]
			rep_count = len(s) // rep_size
			matches = True
			for rep_index in range(rep_count):
				index = rep_index * rep_size
				right = s[index : index + rep_size]
				if check != right:
					matches = False
					break

			if matches:
				return True

		return False

	for a, b in ranges:
		for i in range(a, b + 1):
			if check_invalid(i):
				#print(i)
				total += i

	print(total)

solution_1()
solution_2()
