#Name: CrossWord
#Abstract: Count instances of XMAS in text,
#          including backward, diagonal, and forward


found = 0
line = []
file = open('/home/user/Advent2024/4/Input.txt')
text = file.readlines()
for string in text:
	line.append(string)

print(line[1][1])
print(line[2][1])
