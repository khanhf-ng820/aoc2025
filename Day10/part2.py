from queue import Queue
import pprint
import pulp

# THIS SOLUTION USES EXTERNAL LINEAR PROGRAMMING SOLVER
# Use 'pip install pulp' first before running


filepath = "input.txt"


# [#..##] (0,1,3) (1,4) (0,2) {30,40,10,20,20}
# n buttons
# m lights
# m equations
# a_0 + a_2 = 30
# a_0 + a_1 = 40
# a_2 = 10
# a_0 = 20
# a_1 = 20
# Minimize sigma a_i [i = 0->n-1]



def changeChar(str, idx):
	return str[:idx] + ('#' if str[idx] == '.' else '.') + str[idx + 1:]


answer = 0

with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		components = line.split(' ')

		goal = components[0][1:-1]
		buttons = components[1:-1]
		buttons = list(map(lambda x : list(map(int, x[1:-1].split(','))), buttons))
		counter_goal = list(map(int, components[-1][1:-1].split(',')))
		# print(goal, buttons, counter_goal, sep='\n')
		print(goal, buttons, counter_goal, "BUTTONS: " + str(len(buttons)), sep='\n')

		M = len(goal) # = len(counter_goal)
		N = len(buttons)
		equations_LHS, equations_RHS = [], []

		# Gather linear equations
		for i in range(M):
			rhs = counter_goal[i]
			lhs = []
			for j in range(N):
				if i in buttons[j]:
					lhs.append(j)
			equations_LHS.append(lhs)
			equations_RHS.append(rhs)
		print(equations_LHS, equations_RHS)

		# Frequency mapping
		freq_map = dict()
		for i in range(N):
			freq_map[i] = 0
			for lhs in equations_LHS:
				if i in lhs:
					freq_map[i] += 1

		subanswer = 0
		prob = pulp.LpProblem("SimpleLP", pulp.LpMinimize)
		a = [pulp.LpVariable("a"+str(i+1), 0, None, cat='Integer') for i in range(N)]
		prob += sum(a), "Objective"
		for i in range(len(equations_LHS)):
			lhsPulp = 0
			for button in equations_LHS[i]:
				lhsPulp += a[button]
			prob += lhsPulp == equations_RHS[i], "Constraint" + str(i+1)

		prob.solve()


		print("pulp: ", pulp.value(prob.objective))
		print("subanswer: ", subanswer)
		subanswer = pulp.value(prob.objective)
		answer += subanswer





print(f"THE ANSWER IS {answer} !!!")
