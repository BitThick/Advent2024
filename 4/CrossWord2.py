#Name: CrossWord2
#Abstract: Find diagonally placed, overlapping MAS

import re

found = 0
lines = []
file = open('/home/user/Advent2024/4/Input.txt')
text = file.readlines()
for string in text:
	lines.append(string)

lineCount = -1
maxLines = len(lines)
for line in lines:
	lineCount += 1
	if lineCount == 0 or lineCount == maxLines - 1: continue

	charCount = -1
	safe = True
	lineSize = len(line)
	for char in line:
		charCount += 1
		if charCount == 0 or charCount == lineSize - 1: continue
		if char == 'A':
			goodCount = 0
			if lines[lineCount - 1][charCount - 1] == 'M':								#up-left
				if lines[lineCount + 1][charCount + 1] == 'S': goodCount += 1			#down-right
				else: continue
			if lines[lineCount + 1][charCount - 1] == 'M':								#down-left
				if lines[lineCount - 1][charCount + 1] == 'S':goodCount += 1			#up-right
				else: continue
			if lines[lineCount - 1][charCount + 1] == 'M': 								#up-right
				if lines[lineCount + 1][charCount - 1] == 'S': goodCount += 1			#down-left
				else: continue
			if lines[lineCount + 1][charCount + 1] == 'M':								#down-right
				if lines[lineCount - 1][charCount - 1] == 'S': goodCount += 1			#up-left
			if goodCount == 2: found += 1

print(found)