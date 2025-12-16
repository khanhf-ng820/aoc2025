file_path = "input.txt"

sumInvalid = 0

def invalid(ID):
	length = len(str(ID))
	for i in reversed(range(1, length // 2 + 1)):
		if length % i == 0:
			dividend = 1
			for _ in range(length // i - 1):
				dividend *= 10 ** i
				dividend += 1
			if ID % dividend == 0:
				return True
	return False

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
