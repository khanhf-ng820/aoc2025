from queue import Queue


filepath = "input.txt"



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

		# ----- BFS -----
		N = len(goal)
		q = Queue()
		distance = dict()
		distance['.' * N] = 0
		q.put('.' * N)

		while q.qsize() > 0:
			state = q.get()
			for button in buttons:
				state_tmp = state
				for b in button:
					state_tmp = changeChar(state_tmp, b)
				if state_tmp not in distance:
					distance[state_tmp] = distance[state] + 1
					q.put(state_tmp)

		answer += distance[goal]



print(f"The answer is {answer} !!!")
