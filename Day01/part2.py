file_path = "input.txt"

dial = 50
password = 0

try:
	with open(file_path, 'r') as file:
		for line in file:
			line = line.strip()
			if len(line) < 2:
				continue
			clicks = int(line[1:])
			if line[0] == 'L':
				if dial == 0:
					password += clicks // 100
				elif clicks < dial:
					pass
				else:
					clicks -= dial
					password += 1
					password += clicks // 100
				dial = (dial - int(line[1:])) % 100
			else:
				if dial == 0:
					password += clicks // 100
				elif clicks < 100 - dial:
					pass
				else:
					clicks -= 100 - dial
					password += 1
					password += clicks // 100
				dial = (dial + int(line[1:])) % 100
	
	print(f"The password is: {password}")
except Exception as e:
	print(f"An error occurred: {e}")
