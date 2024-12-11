#Name: CrossWord
#Abstract: Count instances of XMAS in text,
#          including backward, diagonal, and forward

import re

found = 0
lines = []
file = open('/home/user/Advent2024/4/Input.txt')
text = file.readlines()
#text = file.read() try using array notation on this?
for string in text:
	lines.append(string)

lineCount = -1
for line in lines:
	lineCount += 1
	#xmas = re.findall('XMAS', line)
	#for item in xmas:
		#found += 1
	#samx = re.findall('SAMX', line)
	#for item in samx:
		#found += 1

	charCount = -1
	for char in line:
		charCount += 1
		if char == 'X':
			if (lineCount - 3) < 0 or (charCount - 3) < 0: continue
			if lines[lineCount - 1][charCount - 1] == 'M':			#up-left diagonal
				if lines[lineCount - 2][charCount - 2] == 'A':
					if lines[lineCount - 3][charCount - 3] == 'S':
						found += 1
			if (lineCount - 3) < 0 or (charCount + 3) > len(line): continue
			if lines[lineCount - 1][charCount + 1] == 'M':			#up-right diagonal
				if lines[lineCount - 2][charCount + 2] == 'A':
					if lines[lineCount - 3][charCount + 3] == 'S':
						found += 1
			if (lineCount + 3) > (len(lines) - 1) or (charCount + 3) > len(line): continue
			if lines[lineCount + 1][charCount + 1] == 'M':			#down-right diagonal
				if lines[lineCount + 2][charCount + 2] == 'A':
					if lines[lineCount + 3][charCount + 3] == 'S':
						found += 1
			if (lineCount + 3) > (len(lines) - 1) or (charCount - 3) < 0: continue
			if lines[lineCount + 1][charCount - 1] == 'M':			#down-left diagonal
				if lines[lineCount + 2][charCount - 2] == 'A':
					if lines[lineCount + 3][charCount - 3] == 'S':
						found += 1
			if line[charCount - 1] == 'M':							#backwards (tested good)
				if line[charCount - 2] == 'A':
					if line[charCount - 3] == 'S':
						found += 1
			if line[charCount + 1] == 'M':							#forward (tested good)
				if line[charCount + 2] == 'A':
					if line[charCount + 3] == 'S':
						found += 1

print(found)
#2058 is too low