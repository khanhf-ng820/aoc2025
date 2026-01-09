from queue import Queue


filepath = "input.txt"



answer = 0


adjList = dict()


with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		components = line.split(' ')

		components[0] = components[0][:len(components[0]) - 1]

		adjList[components[0]] = set(components[1:])


# ----- BFS -----
counter = dict()
counter['you'] = 1
q = Queue()
q.put('you')

while q.qsize() > 0:
	vertex = q.get()
	if vertex not in adjList:
		continue
	for v in adjList[vertex]:
		if v in counter:
			counter[v] += counter[vertex]
			continue
		counter[v] = counter[vertex]
		q.put(v)


answer = counter['out']






print(f"THE ANSWER IS {answer} !!!")
