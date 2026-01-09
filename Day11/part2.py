from queue import Queue


filepath = "input.txt"



answer1, answer2 = 1, 1


adjList = dict()


with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		components = line.split(' ')

		components[0] = components[0][:len(components[0]) - 1]

		adjList[components[0]] = set(components[1:])



# ----- DFS with DP, counting number of paths -----
dp = dict()
def dfsCountPaths(start, end):
	if start == end:
		return 1
	if start in dp:
		return dp[start]

	paths = 0
	for v in adjList.get(start, []):
		paths += dfsCountPaths(v, end)
	dp[start] = paths
	return paths

def countPaths(start, end):
	global dp
	dp = dict()
	return dfsCountPaths(start, end)





answer1 *= countPaths('svr', 'fft')
print(answer1)
answer1 *= countPaths('fft', 'dac')
print(answer1)
answer1 *= countPaths('dac', 'out')
print(answer1)

answer2 *= countPaths('svr', 'dac')
print(answer2)
answer2 *= countPaths('dac', 'fft')
print(answer2)
answer2 *= countPaths('fft', 'out')
print(answer2)





answer = answer1 + answer2
print(f"THE ANSWER IS {answer} !!!")
