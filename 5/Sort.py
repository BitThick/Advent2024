#Name: Sort
#Abstract: Sum number sequence lines that follow order rules

sum = 0
file = open('/home/user/Advent2024/5/Rules.txt')
fileIn = file.readlines()
rules = []
for item in fileIn:
	rules.append(item[0:-1].split('|') )

file = open('/home/user/Advent2024/5/Pages.txt')
fileIn = file.readlines()
pageSets = []
for item in fileIn:
	pageSets.append(item[0:-1].split(',') )

bad = False
for pageSet in pageSets:
	print(pageSet)
	index = -1									#reset index
	for number in pageSet:
		index += 1
		for rule in rules:								#looking through all rules
			if rule[0] == number:						#applicable rule found
				for item in pageSet[0:index]:		#review previous numbers in set per the rule
					if item == rule[1]:				#follow-number found before, rule broken
						bad = True
						break
		if bad is True: break							#rule broken, stop checking numbers in set
	if bad is True: continue							#skip to next set
	else:														#sum middle value
		length = len(pageSet)
		if length % 2 > 0:
			index = int(length / 2)				#+1 for middle count, canceled by -1 converting to index
			sum += int(pageSet[index])
			print('good')
			print(pageSet[index])

print(sum)
#123 too low