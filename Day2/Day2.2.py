import os.path
import sys
with open(os.path.join(sys.path[0], "input.txt")) as f:
	content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
cont = [list(x.strip()) for x in content]
result = []
def getDiff(lines):
	for i in range(0,(len(lines)-2)):
		for y in range (i+1 , len(lines) - 1 ):
			result = []
			for k in range (0,len(lines[i])):
				if lines[i][k] == lines[y][k]:
					result.append(lines[i][k])
			if len(result) == len(lines[i]) -1:
				return(result)

# print(cont[0][0])
#getDiff(cont)
print(''.join(getDiff(cont)))
