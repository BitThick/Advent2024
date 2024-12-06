#Name: Compare
#Author: R.M.
#Abstract: Pair ints in ascending order from two lists.
#          Sum differences between pairs.

file = open('/home/user/AdventCode24/1/Input.txt')
text = file.readlines()
list1 = []
list2 = []
count = 0
sum = 0

for line in text:
	split = line.split()
	list1.append(int(split[0]) )
	list2.append(int(split[1]) )

list1.sort()
list2.sort()

if len(list1) != len(list2):
	print('failure: lists unequal')
	exit()

while count < 1000:		#0-999 = 1000
	diff = abs(list1[count] - list2[count])
	sum += diff
	count += 1
	#print('|'+str(list1[count])+' - '+str(list2[count])+'| = '+str(diff) )


print('total difference: '+str(sum) ) #2164381