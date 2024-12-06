#Name: Compare2
#Author: R.M.
#Abstract: Gets number of occurences of each list1 number, in list2.
#          Multiplies each list1 number by number of occurence.
#          Sums each of these multiples for a 'similarity score'

file = open('/home/user/AdventCode24/1/Input.txt')
text = file.readlines()
list1 = []
list2 = []

for line in text:
	split = line.split()
	list1.append(int(split[0]) )
	list2.append(int(split[1]) )

list1.sort()
list2.sort()

length1 = len(list1)
#if length1 != len(list2):			#verified equal
#	print('failure: lists unequal')
#	exit()

mark = 0
count = 0
lastNumber = 0
total = 0
for number in list1:
	for index in range(mark, length1):
		if number == list2[index]:
			count += 1
			if count == 1: mark = index	#save list2 index to start next search
			lastNumber = number
		else:
			#if count > 0: print(str(lastNumber)+' '+str(count))
			total += (lastNumber * count)
			count = 0

print(total) #20719933