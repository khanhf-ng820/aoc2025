from queue import Queue
import pprint
import copy



filepath = "input.txt"




tiles = []
tile = []
gettingTileLine = -1


answer = 0


solutionExists = False
pixelPerPresent = []
dimensions = []
requirements = []





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
			solutionExists = 9 * sum(requirements) <= x*y

			if solutionExists:
				print("SOLUTION EXISTS")
				answer += 1
				solutionExists = False
			else:
				print("SOLUTION DOESN\'T EXIST")



pprint.pprint(pixelPerPresent)
pprint.pprint(tiles)




print(f"THE ANSWER IS {answer} !!!")

