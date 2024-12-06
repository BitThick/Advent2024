#Name: Mul
#Abstract: Find number pairs per a pattern, 
#          multiply them & sum the products


import re

file = open('/home/user/Advent2024/3/Input.txt')
text = file.read()
list = re.findall("do\(\).+|\s*don't\(\)", text)
for item in list:
	print(item)
input()
sum = 0
for item in list:
	sub = item[4:-1]
	numbers = sub.split(',')
	total = int(numbers[0]) * int(numbers[1])
	sum += total

print(sum)