#Name: Safe2
#Abstract: Find safe series (per Safe), alow 1 error

file = open('/home/user/AdventCode24/2/Input.txt')
text = file.readlines()
safeCount = 0
for line in text:
	list = line.split()
	index = 0
	for item in list:
		localList = list.copy()
		del localList[index]
		errorCount = 0
		previous = None
		upOnly = None
		for item in localList:
			number = int(item)
			if previous is None:
				previous = number
				continue
			difference = previous - number
			range = abs(difference)
			if range < 1 or range > 3: errorCount += 1
			elif difference > 0:
				if upOnly is False: errorCount += 1
				else: upOnly = True
			elif difference < 0:
				if upOnly is True: errorCount += 1
				else: upOnly = False
			if errorCount > 0: break
			previous = number
		if errorCount == 0:
			safeCount += 1
			break
		index += 1
print(safeCount)