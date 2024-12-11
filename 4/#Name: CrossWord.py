#Name: CrossWord
#Abstract: Count instances of XMAS in text,
#          including backward, diagonal, and forward


found = 0
file = open('/home/user/Advent2024/4/Input.txt')
text = file.read()
for char in text:
	if char == '\n':
		print('nl')
		input()
	else: print(char)


print(found)