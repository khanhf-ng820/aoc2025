file_path = "input.txt"

sumInvalid = 0

def invalid(ID):
	length = len(str(ID))
	if length % 2 != 0:
		return False
	return ID % (10 ** (length // 2) + 1) == 0

try:
	with open(file_path, 'r') as file:
		for line in file:
			line = line.strip()
			ranges = line.split(',')

			for idRange in ranges:
				start, end = idRange.split('-')
				start = int(start)
				end = int(end)
				for i in range(start, end+1):
					if invalid(i):
						sumInvalid += i

	print(f"The answer is: {sumInvalid}")
except Exception as e:
	print(f"An error occurred: {e}")
