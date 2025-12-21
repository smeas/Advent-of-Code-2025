#
# Day 10
# Solution 1: 449
# Solution 2: 17848
#

raw = open("input.txt").read()


def solution_1():
    total = 0
    for line in raw.splitlines():
        # parse goal and buttons as bitsets stored as int
        goal = sum(1 << i for i, c in enumerate(
            line[1:line.index("]")]) if c == "#")
        button_str = line[line.index("("):line.rindex(")") + 1]
        buttons = [
            sum(1 << int(i) for i in group[1:-1].split(",")) for group in button_str.split(" ")]

        # compute while deduplicating
        current_set = {0}
        presses = 0
        while True:
            presses += 1
            # compute all possible state permutations after this round of presses
            current_set = set(
                state ^ button for button in buttons for state in current_set)
            if goal in current_set:
                break

        total += presses

    print(total)


def solution_2():
    # The following input can be broken down into an equation system. The buttons are named a-f.
    # "(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    # (1) 3=e+f
    # (2) 5=b+f
    # (3) 4=c+d+e
    # (4) 7=a+b+d
    #
    # a-f are constrained to be integers that are >= 0.
    #
    # the solution is given by minimizing the sum of all buttons:
    # S=a+b+c+d+e+f

    # I could not figure out how to solve this myself and had to look up how others were solving the equation. I found
    # a library called z3 that is able to solve for these constraints. So here is my implementation using that.
    import z3
    total = 0
    for line in raw.splitlines():
        goal = list(map(int, line[line.index("{")+1:-1].split(",")))
        goal_size = len(goal)
        button_str = line[line.index("("):line.rindex(")") + 1]
        buttons = []
        for group in button_str.split(" "):
            button_set = [0] * goal_size
            for n in map(int, group[1:-1].split(",")):
                button_set[n] = 1
            buttons.append(button_set)

        button_count = len(buttons)
        button_vars = [z3.Int(chr(ord('a') + n))
                       for n in range(button_count)]  # all vars are integers
        solver = z3.Optimize()
        # all vars are >= 0
        solver.add(z3.And([var >= 0 for var in button_vars]))

        equations = []
        for n in range(goal_size):
            coefficients = [buttons[button_index][n]
                            for button_index in range(button_count)]
            equations.append(
                sum(var * btn for var, btn in zip(button_vars, coefficients)) == goal[n])

        solver.add(equations)
        solver.minimize(sum(button_vars))
        solver.check()
        model = solver.model()
        value = sum(model[var].as_long() for var in model.decls())

        total += value

    print(total)


solution_1()
solution_2()
