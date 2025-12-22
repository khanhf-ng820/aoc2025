filepath = "input.txt"



red = []

with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		x, y = list(map(int, line.split(',')))
		red.append([x, y])

maxarea = 0

for t1 in red:
	for t2 in red:
		area = (abs(t2[0] - t1[0]) + 1) * (abs(t2[1] - t1[1]) + 1)
		maxarea = max(area, maxarea)

print(f"The answer is {maxarea} !!!")
