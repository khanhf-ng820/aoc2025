filepath = "input.txt"
# SOLUTION IS NOT TOO EFFICIENT


red = []
edges = []

with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		x, y = list(map(int, line.split(',')))
		red.append([x, y])

for i in range(len(red)-1):
	edges.append([red[i], red[i+1]])
edges.append([red[len(red)-1], red[0]])



# Check point inside boundary using ray casting algorithm
def insideCheck(x, y):
	for edge in edges:
		xa, ya = edge[0]
		xb, yb = edge[1]
		if ((xa <= x and x <= xb) or (xa >= x and x >= xb)) and ((ya <= y and y <= yb) or (ya >= y and y >= yb)):
			return True
	vertCount = 0
	horiCount = 0
	x += 0.1
	y += 0.1
	for edge in edges:
		xa, ya = edge[0]
		xb, yb = edge[1]
		if xa == xb and xa > x and y > min(ya, yb) and y <= max(ya, yb):
			vertCount += 1

	return vertCount % 2 == 1



maxarea = 0


for t1 in red:
	for t2 in red:
		x1, y1 = t1
		x2, y2 = t2
		x3, y3 = x1, y2
		x4, y4 = x2, y1
		
		allowed = True
		# Check no other vertex is inside rectangle
		for t in red:
			xa, ya = t
			if xa > min(x1, x2) and xa < max(x1, x2) and ya > min(y1, y2) and ya < max(y1, y2):
				allowed = False
				break
		if not allowed:
			continue

		# Check if no other edges intersect the rectangle
		for edge in edges:
			xa, ya = edge[0]
			xb, yb = edge[1]
			if xa == xb and min(x1, x2) < xa and xa < max(x1, x2) and min(ya, yb) < max(y1, y2) and max(ya, yb) > min(y1, y2):
				allowed = False
				break
			if ya == yb and min(y1, y2) < ya and ya < max(y1, y2) and min(xa, xb) < max(x1, x2) and max(xa, xb) > min(x1, x2):
				allowed = False
				break
		if not allowed:
			continue

		# Check all 4 vertices of rectangle is inside boundary
		if not (insideCheck(x1, y1) and insideCheck(x2, y2) and insideCheck(x3, y3) and insideCheck(x4, y4)):
			continue





		area = (abs(t2[0] - t1[0]) + 1) * (abs(t2[1] - t1[1]) + 1)
		# print(t1, t2, area)
		maxarea = max(area, maxarea)



print(f"The answer is {maxarea} !!!")
