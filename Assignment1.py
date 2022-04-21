import math

list1 = [7.0, 0.0]
list2 = [3.0, 3.0]
i = 0
sum = 0

for items in list1:
	sum = sum + (list1[i] - list2[i]) * (list1[i] - list2[i])
	i = i + 1

var = math.sqrt(sum)
print(var)	