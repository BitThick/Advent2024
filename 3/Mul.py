#Name: Mul
#Abstract: Find number pairs per a pattern, 
#          multiply them & sum the products


import re

file = open('/home/user/AdventCode24/3/Input.txt')
text = file.read()
list = re.findall('mul\(\d+,\d+\)', text)
sum = 0
for item in list:
	sub = item[4:-1]
	numbers = sub.split(',')
	total = int(numbers[0]) * int(numbers[1])
	sum += total

print(sum)