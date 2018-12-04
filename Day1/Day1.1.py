import os.path
import sys
with open(os.path.join(sys.path[0], "input.txt")) as f:
	content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
result = 0
for line in content:
	result += line
print(result)
