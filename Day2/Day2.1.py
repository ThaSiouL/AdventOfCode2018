import os.path
import sys
with open(os.path.join(sys.path[0], "input.txt")) as f:
	content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [sorted(list(x.strip())) for x in content]
doubles = 0
triples = 0
for line in content:
	lastchar = ""
	counter = 0
	foundDouble = 0
	foundTripple = 0
	for currChar in line:
		if lastchar == currChar:
			counter += 1
		else:
			if counter == 2:
				foundDouble = 1
			elif counter == 3:
				foundTripple = 1
			counter = 1
			lastchar = currChar
	if counter == 2:
		foundDouble = 1
	elif counter == 3:
		foundTripple = 1
	doubles += foundDouble
	triples += foundTripple


print(doubles * triples)
