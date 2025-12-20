filepath = "input.txt"



points = []
pairs = []
connections = dict()

# DFS Components
visited = set()
components = []
component = []

def distsq(p1, p2):
	return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def dfs(p):
	tuple_p = tuple(p)
	if tuple_p in visited:
		return
	visited.add(tuple_p)
	component.append(p)
	if tuple_p not in connections:
		return
	for v in connections[tuple_p]:
		dfs(list(v))


with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		xyz = line.split(',')
		xyz = list(map(lambda x : int(x), xyz))
		points.append(xyz)

for i in range(len(points)):
	for j in range(i+1, len(points)):
		p1 = points[i]
		p2 = points[j]
		if p1 == p2:
			continue
		pairs.append([p1, p2, distsq(p1, p2)])

pairs.sort(key=(lambda x : x[2]))

for i in range(len(pairs)):
	if tuple(pairs[i][0]) not in connections:
		connections[tuple(pairs[i][0])] = []
	connections[tuple(pairs[i][0])].append(tuple(pairs[i][1]))
	if tuple(pairs[i][1]) not in connections:
		connections[tuple(pairs[i][1])] = []
	connections[tuple(pairs[i][1])].append(tuple(pairs[i][0]))

	# DFS
	components = []
	visited = set()
	for p in points:
		component = []
		dfs(p)
		if len(component) > 0:
			components.append(component)

	if len(components) == 1:
		answer = pairs[i][0][0] * pairs[i][1][0]
		print(f"The answer is: {answer} !!!")
		break
