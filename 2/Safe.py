#Name: Safe
#Author: R.M.
#Abstract: Checks each set (line) of numbers,
#          ensuring they iterate only up or down,
#          by 1-3.

file = open('/home/user/AdventCode24/2/Input.txt')
text = file.readlines()
list = []

safeCount = 0
for line in text:
	up = True
	down = True
	rangeOk = True
	list = line.split()
	lastNumber = int(list[0])
	for item in list[1:]:
		number = int(item)
		difference = number - lastNumber
		absolute = abs(difference)
		if absolute >= 1 and absolute <= 3:
			if difference > 0: down = False
			else: up = False
			if up is False and down is False: break
		else:
			rangeOk = False
			break
		lastNumber = number

	if rangeOk is True and (up is True or down is True):
		safeCount += 1

print('safe sets: '+ str(safeCount) )