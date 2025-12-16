file_path = "input.txt"

dial = 50
password = 0

try:
	with open(file_path, 'r') as file:
		for line in file:
			line = line.strip()
			if len(line) < 2:
				continue
			if line[0] == 'L':
				dial = (dial - int(line[1:])) % 100
			else:
				dial = (dial + int(line[1:])) % 100
			if dial == 0:
				password += 1
	
	print(f"The password is: {password}")
except Exception as e:
	print(f"An error occurred: {e}")
