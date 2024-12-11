#Name: Mul2
#Abstract: Find number pairs per a pattern
#          & between do() * don't(), then
#          multiply them & sum the products

import re

sum = 0
file = open('/home/user/Advent2024/3/Input.txt')
text = file.read()
do = re.findall("do\(\)([\s\S]*?)don't\(\)", text)
for item in do:
	mul = re.findall('mul\(\d+,\d+\)', item)
	for pair in mul:
		sub = pair[4:-1]
		numbers = sub.split(',')
		total = int(numbers[0]) * int(numbers[1])
		sum += total

print(sum)