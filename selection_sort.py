import datetime
from random import randint

def create_arr():
	arr = []
	for i in range(1, 10001):
		arr.append(randint(1,10000))
	return arr

t1 = datetime.datetime.today()

# def selection_sort(arr):
# 	i = 0
# 	while i < len(arr):
# 		j = i
# 		while j < len(arr):
# 			temp = arr[i]
# 			if arr[i] > arr[j]:
# 				arr[i] = arr[j]
# 				arr[j] = temp
# 			j += 1
# 		i += 1
# 	return arr

def selection_sort(arr):
	i = 0
	while i < len(arr):
		j = i
		min = i
		while j < len(arr):
			if arr[i] > arr[j]:
				min = j
			j += 1
		if (min != i):
			temp = arr[i]
			arr[i] = arr[min]
			arr[min] = temp
		i+= 1
	return arr

arr = create_arr()
print selection_sort(arr)
t2 = datetime.datetime.today()
print (t2 - t1)

