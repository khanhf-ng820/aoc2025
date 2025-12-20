filepath = "input.txt"
NUM_OF_CONNECTIONS = 1000



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

for i in range(NUM_OF_CONNECTIONS):
	if tuple(pairs[i][0]) not in connections:
		connections[tuple(pairs[i][0])] = []
	connections[tuple(pairs[i][0])].append(tuple(pairs[i][1]))
	if tuple(pairs[i][1]) not in connections:
		connections[tuple(pairs[i][1])] = []
	connections[tuple(pairs[i][1])].append(tuple(pairs[i][0]))

# DFS
for p in points:
	component = []
	dfs(p)
	components.append(component)

components.sort(key=(lambda x : len(x)), reverse=True)

answer = len(components[0]) * len(components[1]) * len(components[2])

print(f"The answer is: {answer} !!!")
