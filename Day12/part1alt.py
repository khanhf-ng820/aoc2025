from queue import Queue
import pprint
import copy



filepath = "test.txt"


def rotate90(matrix):
	return [list(row) for row in zip(*matrix[::-1])]
def flip_horizontal(matrix):
	return [row[::-1] for row in matrix]
def flip_vertical(matrix):
	return matrix[::-1]
# 8 states:
# 4 rotations
# Horizontal flip
# Vertical flip
# Horizontal flip + 90 deg rotation
# Vertical flip + 90 deg rotation
def permutate(matrix, idx):
	if idx == 0:
		return copy.deepcopy(matrix)
	elif idx == 1:
		return rotate90(matrix)
	elif idx == 2:
		return rotate90(rotate90(matrix))
	elif idx == 3:
		return rotate90(rotate90(rotate90(matrix)))
	elif idx == 4:
		return flip_horizontal(matrix)
	elif idx == 5:
		return flip_vertical(matrix)
	elif idx == 6:
		return flip_horizontal(rotate90(matrix))
	elif idx == 7:
		return flip_vertical(rotate90(matrix))


tiles = []
tile = []
gettingTileLine = -1


answer = 0


solutionExists = False
pixelPerPresent = []
dimensions = []
requirements = []
visited = set()



class State:
	def __init__(self, collisionArr):
		self.colArr = collisionArr
		self.tileCount = 0
	def __str__(self):
		return f"Object: {self.colArr}\ntile count: {self.tileCount}"
	def stateKey(self):
		return (
			self.tileCount,
			tuple(tuple(tuple(s) for s in row) for row in self.colArr)
		)
	def numOfTiles(self):
		return self.tileCount
	def accept(self):
		return sum(requirements) == self.numOfTiles()
	def early_reject(self, r, c):
		# Faster by considering 3x3 region only
		for i in range(r, r+3):
			for j in range(c, c+3):
				if len(self.colArr[i][j]) > 1:
					return True
		return False
	def reject(self):
		emptyPixels = 0
		for row in self.colArr:
			for s in row:
				if len(s) > 1:
					# Pruning: Reject overlapping
					return True
				elif len(s) == 0:
					emptyPixels += 1
		# Pruning 1
		remainingPixels = 0 # Remaining pixels needed to add
		tileCount = self.tileCount
		for i in range(len(requirements)):
			if tileCount >= requirements[i]:
				tileCount -= requirements[i]
			else:
				remainingPixels += (requirements[i] - tileCount) * pixelPerPresent[i]
				tileCount = 0
		if emptyPixels < remainingPixels:
			return True

		return False
	def getCurTileIdx(self): # index in 'tiles' array
		curTile = self.numOfTiles()
		for i in range(len(requirements)):
			tileSum = sum(requirements[:i+1])
			if curTile <= tileSum:
				return i
		return None
	def getNextTileIdx(self): # index in 'tiles' array
		if self.accept():
			return None
		curTile = self.numOfTiles()
		nextTile = curTile + 1
		for i in range(len(requirements)):
			tileSum = sum(requirements[:i+1])
			if nextTile <= tileSum:
				return i
		print(nextTile)
		return None
	def precheck(self, r, c, permIdx):
		# Precheck valid before applying
		tileIdx = self.getNextTileIdx()
		if tileIdx == None:
			return False
		presentMat = permutate(tiles[tileIdx], permIdx)
		for i in range(3):
			for j in range(3):
				if presentMat[i][j] == '#':
					if len(self.colArr[r+i][c+j]) > 0:
						return False
		return True
	def apply(self, r, c, permIdx):
		tileIdx = self.getNextTileIdx()
		if tileIdx == None:
			return False
		presentMat = permutate(tiles[tileIdx], permIdx)
		self.tileCount += 1
		for i in range(3):
			for j in range(3):
				if presentMat[i][j] == '#':
					self.colArr[r+i][c+j].add(self.tileCount)
		return True
	def undo(self, r, c, permIdx):
		tileIdx = self.getCurTileIdx()
		if tileIdx == None:
			return False
		presentMat = permutate(tiles[tileIdx], permIdx)
		for i in range(3):
			for j in range(3):
				if presentMat[i][j] == '#':
					self.colArr[r+i][c+j].remove(self.tileCount)
		self.tileCount -= 1
		return True
	def choices(self):
		tileIdx = self.getNextTileIdx()
		if tileIdx == None:
			return []
		w, h = dimensions
		return [(i, j, perm) for i in range(h-2) for j in range(w-2) for perm in range(8)]
		# allChoices = set()
		# for i in range(h-2):
		# 	for j in range(w-2):
		# 		for perm in range(8):
		# 			# if self.precheck(i, j, perm):
		# 			allChoices.add((i, j, perm))
		# return allChoices



# Backtracking function
def backtrack(state):
	global solutionExists
	# Terminate when found solution
	if solutionExists:
		return
	# Check visited state
	key = state.stateKey()
	if key in visited:
		return
	visited.add(key)
	if state.reject():
		# print(state, " REJECTED")
		print(len(visited))
		return
	if state.accept():
		print(state)
		solutionExists = True
		return
	for choice in state.choices():
		apply_check = state.apply(*choice)
		if not apply_check:
			print("apply_check is False")
		# Fast reject early
		if state.early_reject(*choice[0:2]):
			print(len(visited))
			undo_check = state.undo(*choice)
			if not undo_check:
				print("undo_check is False")
			continue
		backtrack(state)
		undo_check = state.undo(*choice)
		if not undo_check:
			print("undo_check is False")





with open(filepath, 'r') as file:
	for line in file:
		line = line.strip()
		# Reading all tiles
		if len(line) == 2:
			gettingTileLine = 0
			tile = []
		elif len(line) == 0:
			gettingTileLine = -1
			tiles.append(tile)
			# Get # of pixels for each present
			pixelPerPresent.append(sum(row.count('#') for row in tile))
		elif gettingTileLine == 0:
			tile.append(line)
		elif len(line) > 3:
			# Regions
			print(line)
			components = line.split(':')
			x, y = list(map(int, components[0].split('x')))
			dimensions = [x, y]
			requirements = list(map(int, components[1].strip().split(' ')))
			state = State(
				[[set() for i in range(x)] for j in range(y)]
			)
			visited.clear()
			backtrack(state)
			# print(len(visited))

			if solutionExists:
				print("SOLUTION EXISTS")
				answer += 1
				solutionExists = False
			else:
				print("SOLUTION DOESN\'T EXIST")



pprint.pprint(pixelPerPresent)
pprint.pprint(tiles)




print(f"THE ANSWER IS {answer} !!!")
